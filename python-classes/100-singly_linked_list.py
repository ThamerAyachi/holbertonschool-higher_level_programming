#!/usr/bin/python3
"""Single linked list with python"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None) -> None:

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self) -> int:
        return self.__data

    @data.setter
    def data(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def next_node(self, value) -> None:
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
