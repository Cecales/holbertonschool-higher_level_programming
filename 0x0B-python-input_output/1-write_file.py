#!/usr/bin/python3
"""
Module 1-write_file
wirtes a text in a file
"""


def write_file(filename="", text=""):
    """
    write text in a file with filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
