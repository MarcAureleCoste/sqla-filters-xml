# -*- coding: utf-8 -*-
"""sqla-filters-xml setup file."""
import os
from typing import List
from setuptools import setup

NAME: str = 'sqla-filters-xml'
VERSION: str = '0.0.1'
DESCRIPTION: str = 'XML parser for sqla-filters.'

def get_requirements() -> List[str]:
    """Return the requirements as a list of strings."""
    requirements_path = os.path.join(
        os.path.dirname(__file__), 'requirements.txt'
    )
    with open(requirements_path) as f:
        return f.read().split()

def read(file_path: str):
    """Simply return the content of a file."""
    with open(file_path) as f:
        return f.read()

REQUIRE = get_requirements()
DEV_REQUIRE = [
    'pylint',
    'pep8',
    'autopep8',
    'ipython',
    'mypy',
    'pytest',
    'rope',
    'sphinx',
    'twine'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.md')),
    long_description_content_type='text/markdown',
    url='https://github.com/MarcAureleCoste/sqla-filters-xml',

    author='Marc-Aurele Coste',

    license='MIT',
    zip_safe=False,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=REQUIRE,
    packages=(
        'sqla_filters.parser.xml',
    ),
    package_dir={'': 'src'},
    entry_points={},

    test_require=DEV_REQUIRE,
    extras_require={
        'dev': DEV_REQUIRE
    }
)