#!/usr/bin/python3
"""Single linked list with python"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None) -> None:
        """initial class"""

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if not isinstance(next_node, Node) and next_node is not None:
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


class SinglyLinkedList:
    """Singly Linked List class"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current: Node = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
