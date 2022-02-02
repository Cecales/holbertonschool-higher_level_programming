#!/usr/bin/python3
"""
Module 5-save_to_json_file
Writes an object to a text file,
usinga a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes the representation
    of my_obj to filename
    """

    with open(filename, "w", encoding="utf-8") as r:
        r.write(json.dumps(my_obj))
