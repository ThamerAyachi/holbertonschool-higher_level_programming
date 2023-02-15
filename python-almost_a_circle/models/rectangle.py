#!/usr/bin/python3
"""Create class Rectangle"""
from models.base import Base


class Rectangle (Base):
    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width > 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height > 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not x >= 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not y >= 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self) -> int:
        """get width"""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self) -> int:
        """get height"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self) -> int:
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if not value >= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self) -> int:
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if not value >= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get area of this rectangle"""
        return self.__height * self.__width
