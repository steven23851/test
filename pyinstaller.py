#!/usr/bin/env python3

import PyInstaller.__main__
import os

OS_NAME = os.environ.get("MATRIX_OS")
OS_ARCH = os.environ.get("MATRIX_ARCH")


name = "test-application-{}-{}".format(OS_NAME, OS_ARCH)

PyInstaller.__main__.run([
    "--onefile",
    "--console",
    "--name", name,
    "--workpath", "build",
    "--specpath", "build",
    "application/__main__.py",
])
