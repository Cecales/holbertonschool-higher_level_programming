#!/usr/bin/python3
"""
Module 0-read_file
Reads values from a file and prints
"""


def read_file(filename=""):
    """
    Read a file with filename
    and prints its content to stdout
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
