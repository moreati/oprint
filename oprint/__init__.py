import pprint as _stdlib_pprint


__all__ = [
    "pprint",
    "pformat",
    "isreadable",
    "isrecursive",
    "saferepr",
    "PrettyPrinter",
]


def pprint(object, stream=None, indent=1, width=80, depth=None, *,
           compact=False):
    """Pretty-print a Python object to a stream [default is sys.stdout]."""
    printer = PrettyPrinter(
        stream=stream, indent=indent, width=width, depth=depth,
        compact=compact)
    printer.pprint(object)


def pformat(object, indent=1, width=80, depth=None, *, compact=False):
    """Format a Python object into a pretty-printed representation."""
    return PrettyPrinter(indent=indent, width=width, depth=depth,
                         compact=compact).pformat(object)


def saferepr(object):
    """Version of repr() which can handle recursive data structures."""
    return _safe_repr(object, {}, None, 0)[0]


def isreadable(object):
    """Determine if saferepr(object) is readable by eval()."""
    return _safe_repr(object, {}, None, 0)[1]


def isrecursive(object):
    """Determine if object requires a recursive representation."""
    return _safe_repr(object, {}, None, 0)[2]


_safe_key = _stdlib_pprint._safe_key


_safe_tuple = _stdlib_pprint._safe_tuple


class PrettyPrinter(_stdlib_pprint.PrettyPrinter):
    _dispatch = dict(_stdlib_pprint.PrettyPrinter._dispatch)

    def _pprint_dict(self, object, stream, indent, allowance, context, level):
        print('foo')
        write = stream.write
        write('{')
        if self._indent_per_level > 1:
            write((self._indent_per_level - 1) * ' ')
        length = len(object)
        if length:
            # Don't sort the keys, preserve insertion order
            items = object.items()
            self._format_dict_items(items, stream, indent, allowance + 1,
                                    context, level)
        write('}')

    _dispatch[dict.__repr__] = _pprint_dict

    def _pprint_set(self, object, stream, indent, allowance, context, level):
        if not len(object):
            stream.write(repr(object))
            return
        typ = object.__class__
        if typ is set:
            stream.write('{')
            endchar = '}'
        else:
            stream.write(typ.__name__ + '({')
            endchar = '})'
            indent += len(typ.__name__) + 1
        object = object
        self._format_items(object, stream, indent, allowance + len(endchar),
                           context, level)
        stream.write(endchar)

    _dispatch[set.__repr__] = _pprint_set
    _dispatch[frozenset.__repr__] = _pprint_set

    def format(self, object, context, maxlevels, level):
        """Format object for a specific context, returning a string
        and flags indicating whether the representation is 'readable'
        and whether the object represents a recursive construct.
        """
        return _safe_repr(object, context, maxlevels, level)


def _safe_repr(object, context, maxlevels, level):
    typ = type(object)
    if typ in _builtin_scalars:
        return repr(object), True, False

    r = getattr(typ, "__repr__", None)
    if issubclass(typ, dict) and r is dict.__repr__:
        if not object:
            return "{}", True, False
        objid = id(object)
        if maxlevels and level >= maxlevels:
            return "{...}", False, objid in context
        if objid in context:
            return _recursion(object), False, True
        context[objid] = 1
        readable = True
        recursive = False
        components = []
        append = components.append
        level += 1
        saferepr = _safe_repr
        items = object.items()
        for k, v in items:
            krepr, kreadable, krecur = saferepr(k, context, maxlevels, level)
            vrepr, vreadable, vrecur = saferepr(v, context, maxlevels, level)
            append("%s: %s" % (krepr, vrepr))
            readable = readable and kreadable and vreadable
            if krecur or vrecur:
                recursive = True
        del context[objid]
        return "{%s}" % ", ".join(components), readable, recursive

    return _stdlib_pprint._safe_repr(object, context, maxlevels, level)


_builtin_scalars = _stdlib_pprint._builtin_scalars


def _recursion(object):
    return _stdlib_pprint._recursion(object)


def _perfcheck(object=None):
    import time
    if object is None:
        object = [("string", (1, 2), [3, 4], {5: 6, 7: 8})] * 100000
    p = PrettyPrinter()
    t1 = time.time()
    _safe_repr(object, {}, None, 0)
    t2 = time.time()
    p.pformat(object)
    t3 = time.time()
    print("_safe_repr:", t2 - t1)
    print("pformat:", t3 - t2)


del _stdlib_pprint


if __name__ == "__main__":
    _perfcheck()
