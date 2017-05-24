"""
A collection of functions which can be used as a custom type for argparse.
"""

import os
import sys


def abs_existing_file(file):
    file = os.path.abspath(file)
    if not os.path.isfile(file):
        print("Error! File does not exist: \n    "+file)
        sys.exit(1)
    return file
