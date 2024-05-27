#!/usr/bin/env python3

import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--os")
    parser.add_argument("-a", "--arch")
    parser.add_argument("-l", "--label")
    parser.add_argument("-p", "--print", action="store_true")
    args = parser.parse_args()

    if args.label:
        label = args.label
    else:
        label = ""
        if args.os:
            os = args.os.partition("-")[0].lower()
            if os == "ubuntu":
                os = "linux"
            label += os
        if args.arch and args.arch == "x86":
            label += "_x86"

    if args.print:
        return print(label)

    name = "test-application"
    if label:
        name += "_" + label

    import PyInstaller.__main__
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
