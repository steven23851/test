#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="test-application",
    version="0.1.0",
    url="https://github.com/steven23851/test",
    author="Steven",
    author_email="steven23851@proton.me",
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "test = application:main",
        ],
    },
    packages=[
        "application",
    ],
)
