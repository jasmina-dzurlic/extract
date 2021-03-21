#!/usr/bin/env python
"""
Install extract package. To install locally use:
	pip install -e .
"""

from setuptools import setup

setup(
    name="extract",
    version="0.0.1",
    entry_points={
        'console_scripts': ['extract = extract:extract']
    }
)