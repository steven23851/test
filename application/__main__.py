import sys

if not __package__ and not hasattr(sys, "frozen"):
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import application

if __name__ == "__main__":
    sys.exit(application.main())
