#!/usr/bin/python3
"""
models/base.py
"""


import json


class Base:
    """

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """

        """

        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(l):
        """"""
        if l is None or len(l) == 0:
            return "[]"
        return json.dumps(l)

    @classmethod
    def save_to_file(cls, l):
        """"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if l is None:
                f.write(Base.to_json_string([]))
            else:
                li = []
                for obj in l:
                    li.append(obj.to_dictionary())
                f.write(Base.to_json_string(li))

    @staticmethod
    def from_json_string(json_s):
        """"""
        if json_s is None or not json_s:
            return []
        else:
            return json.loads(json_s)
