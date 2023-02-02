#!/usr/bin/python3
"""Module have text_indentation"""


def text_indentation(text) -> None:
    """_summary_

    Args:
        text (string)

    Raises:
        TypeError: text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        if char in ".?:":
            new_text += char + "\n\n"
        else:
            new_text += char
    print(new_text, end='')
