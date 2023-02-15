#!/usr/bin/python3
"""Create Square class"""
from models.rectangle import Rectangle


class Square (Rectangle):
    """Square Class"""

    def __init__(self, size,  x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )
