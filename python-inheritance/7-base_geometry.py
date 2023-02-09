#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self) -> None:
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
