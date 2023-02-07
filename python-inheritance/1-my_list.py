#!/usr/bin/python3
"""My list module"""


class MyList (list):
    """Create my list"""

    def print_sorted(self):
        print(sorted(self))
