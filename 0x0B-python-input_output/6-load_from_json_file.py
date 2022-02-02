#!/usr/bin/python3
"""
Module 6-load_from_json_file
Creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from filename
    """
    with open(filename, "r", encoding="utf-8") as f:
        json_obj = f.read()
        if not len(json_obj):
            return None
        return json.loads(json_obj)
