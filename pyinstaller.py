#!/usr/bin/env python3

import PyInstaller.__main__
import os


PyInstaller.__main__.run([
    "--onefile",
    "--console",
    "--name", "test-application" + os.environ.get("EXE_NAME"),
    "--workpath", "build",
    "--specpath", "build",
    "application/__main__.py",
])
