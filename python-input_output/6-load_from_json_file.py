#!/usr/bin/python3
"""Get Obj from json file"""
import json


def load_from_json_file(filename):
    """Get Obj from json file function"""
    with open(filename, "r", encoding='utf8') as json_file:
        obj = json_file.readlines()
        return json.loads(obj)
