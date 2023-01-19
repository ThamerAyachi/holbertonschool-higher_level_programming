#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 1:
        print("1 argument:")
    elif len(sys.argv) == 1:
        print("0 argument.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
