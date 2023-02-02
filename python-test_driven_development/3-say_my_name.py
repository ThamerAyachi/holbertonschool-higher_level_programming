#!/usr/bin/python3
"""module have say_my_name method"""


def say_my_name(first_name, last_name="") -> None:
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
