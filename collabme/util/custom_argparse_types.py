"""
A collection of functions which can be used as a custom type for argparse.
"""

import os
import sys

from argparse import ArgumentTypeError


def positive_int(string):
    """
    Ensure a positive integer. Else, raise an exception.
    """
    int_ = int(string)
    if int_  < 0:
        raise ArgumentTypeError('{} is not a positive integer'.format(int_))
    return int_


def abs_existing_file(string):
    """
    Ensure the file exists, it is a file, and return the absolute path to the
    directory. Else, raise an exception.
    """
    file_ = os.path.abspath(string)
    if not os.path.isfile(file_):
        raise ArgumentTypeError('File does not exist:\n    {}'.format(file_))
    return file_
