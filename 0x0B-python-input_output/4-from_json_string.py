#!/usr/bin/python3
"""
Module 4-from_json_string
Returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Return the object represented by my_str
    """
    return json.loads(my_str)
