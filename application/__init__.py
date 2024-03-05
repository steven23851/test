import sys

version = "0.1.4"


def main():
    # comment
    sys.stdout.write(f"{version}\n")
    sys.stdout.write("\n".join(sys.argv) + "\n")
    return 0
