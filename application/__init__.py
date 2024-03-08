import sys
from . import version


def main():
    # comment2
    sys.stdout.write(f"{version.__version__}\n")
    sys.stdout.write("\n".join(sys.argv) + "\n")
    return 0
