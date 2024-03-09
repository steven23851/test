#!/usr/bin/env python3

import sys
import argparse
import PyInstaller.__main__


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--os")
    parser.add_argument("-a", "--arch")
    args = parser.parse_args()

    name = "test-application"
    if args.os:
        name = "{}_{}".format(name, args.os.partition("-")[0].lower())
    if args.arch and args.arch == "x86":
        name += "_x86"

    return PyInstaller.__main__.run([
        "--onefile",
        "--console",
        "--name", name,
        "--workpath", "build",
        "--specpath", "build",
        "application/__main__.py",
    ])


if __name__ == "__main__":
    sys.exit(main())
