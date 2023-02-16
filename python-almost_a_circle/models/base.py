#!/usr/bin/python3
"""Create Base class"""
import json


class Base:
    """Base class have private and public instance"""

    __nb_object = 0

    def __init__(self, id=None) -> None:
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """make dictionary in json string format"""
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save data in file"""
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string: str):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
