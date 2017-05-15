======
oprint
======

.. image:: https://travis-ci.org/moreati/oprint.svg?branch=master
    :target: https://travis-ci.org/moreati/oprint
    :alt: Build Tests

A ``pprint`` for CPython 3.6 ``dict`` objects that preserves insertion order.

About
=====

CPython 3.6 uses a new "compact" representation for `dict`_ objects. As a
nice side effect this happens to preserve the insertion order of keys.

    The order-preserving aspect of this new implementation is considered an
    implementation detail and should not be relied upon

``pprint.pprint()`` retains it's behaviour from earlier Python releases.
It formats a ``dict`` object by sorting the keys alphabetically.

.. code:: python

    >>> import pprint
    >>> pprint.pprint({'foo': 1, 'bar': 2, 'baz': 3})
    {'bar': 2, 'baz': 3, 'foo': 1}

``oprint.pprint()`` throws out the old.

.. code:: python

    >>> import oprint
    >>> oprint.pprint({'foo': 1, 'bar': 2, 'baz': 3})
    {'foo': 1, 'bar': 2, 'baz': 3}

The library is otherwise a drop-in replacement for ``pprint``.

Install
=======

.. code:: sh

    pip install oprint

Development
===========

This project is developed on `GitHub`_, please file `issues`_ for any feature
or bug requests.

Contributors
============

- `Alex Willmer`_

.. _pprint.pprint(): https://docs.python.org/3.6/library/pprint.html
.. _dict: https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-compactdict
.. _GitHub: https://github.com/moreati/oprint
.. _issues: https://github.com/moreati/oprint/issues
.. _Alex Willmer: https://github.com/moreati

