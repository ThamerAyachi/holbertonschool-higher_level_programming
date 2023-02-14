#!/usr/bin/python3
"""Create class Rectangle"""
from models.base import Base


class Rectangle (Base):
    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """set width"""
        self.width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """set height"""
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
