#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) is not True:
            return self.__dict__
        else:
            store_dict = self.__dict__
            only_name = {}
            for keys, value in store_dict.items():
                for i in attrs:
                    if keys == i:
                        only_name[keys] = value
            return only_name
