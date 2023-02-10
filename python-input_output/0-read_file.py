#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file function"""
    with open(filename, "r") as f:
        for line in f.readlines():
            print(line, end="")
