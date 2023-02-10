#!/usr/bin/python3
import json
"""String to JSON"""


def to_json_string(my_obj) -> str:
    """_summary_

    Args:
        my_obj (_type_): _description_

    Returns:
        str: _description_
    """
    return json.dumps(my_obj)
