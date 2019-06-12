#!/usr/bin/python3
"""Module base"""
import json


class Base:
    """Base and everything"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a string representation to a file"""
        filename = cls.__name__ + ".json"
        new_list = []
        for i in list_objs:
            new_list.append(i.to_dictionary())
        with open(filename, "w") as f:
            string = cls.to_json_string(new_list)
            f.write(string)
