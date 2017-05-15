import os
import sys

from setuptools import find_packages, setup

"A pprint for CPython 3.6 dict objects that preserves insertion order."

if sys.version_info[0:2] != (3, 6):
    raise ValueError('This package requires CPython 3.6')

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.rst')) as readme:
    long_description = readme.read()

setup(
    name = 'oprint',
    version = '0.1',
    description = __doc__,
    long_description = long_description,
    classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
    ],
    author = "Alex Willmer",
    author_email = "alex@moreati.org.uk",
    url = "https://github.com/moreati/oprint",
    packages = find_packages(),
    platforms = "ALL",
    keywords = [
        "pprint",
    ],
    extras_require = {
        'test': [
            'pytest',
        ],
    },
)
