#!/usr/bin/python3
"""String to JSON"""
import json


def to_json_string(my_obj) -> str:
    """Obj to JSON"""
    return json.dumps(my_obj)
