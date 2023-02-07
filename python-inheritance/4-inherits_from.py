#!/usr/bin/python3
"""Inherits from"""


def inherits_from(obj, a_class):
    """Inherits from"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
