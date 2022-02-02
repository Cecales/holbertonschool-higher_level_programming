#!/usr/bin/python3
"""
Module 2-append_write
Appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends text to filename
    and returns the number of characters added
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
