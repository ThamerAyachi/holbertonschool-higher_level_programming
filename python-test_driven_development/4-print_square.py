#!/usr/bin/python3
"""Module have print_square"""


def print_square(size) -> None:
    """_summary_

    Args:
        size (integer)

    Raises:
        TypeError: size must be an integer
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not (isinstance(size, int) or isinstance(size, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
