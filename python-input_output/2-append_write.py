#!/usr/bin/python3
"""Write file"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, 'a', encoding='utf8') as f:
        f.write(text)
    return len(text)
