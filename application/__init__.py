import sys

version = "0.1.5"


def main():
    # comment2
    sys.stdout.write(f"{version}\n")
    sys.stdout.write("\n".join(sys.argv) + "\n")
    return 0
