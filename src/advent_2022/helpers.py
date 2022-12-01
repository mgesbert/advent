import os
import sys


def get_input():
    dir_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    with open(os.path.join(dir_path, "data.txt")) as f:
        for l in f:
            yield l.strip()
