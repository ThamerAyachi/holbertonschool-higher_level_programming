#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        if i == 8 and j == 9:
            print("{}".format(i*10+j))
        elif (i != 0) and i == j:
            continue
        else:
            print("{:02d}".format(i*10+j), end=", ")
