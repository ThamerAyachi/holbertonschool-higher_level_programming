#!/usr/bin/python3
import sys
"""nQueens"""

if __name__ == "__main__":
    argv = sys.argv
    argv_length = len(argv)

    if argv_length == 1:
        print("Usage: nqueens N")
        exit(1)

    n = argv[1]

    if not n.isdigit():
        print("N must be a number")
        exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        exit(1)
