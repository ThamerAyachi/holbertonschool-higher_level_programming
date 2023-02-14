#!/usr/bin/python3
"""Create Base class"""


class Base:
    """Base class have private and public instance"""

    __nb_object = 0
    id: int

    def __init__(self, id=None) -> None:
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
