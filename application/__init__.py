import sys

version = "0.1.3"


def main():
    sys.stdout.write(f"{version}\n")
    sys.stdout.write("\n".join(sys.argv) + "\n")
    return 0
