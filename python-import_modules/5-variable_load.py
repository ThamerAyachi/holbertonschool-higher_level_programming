#!/usr/bin/python3
from importlib import import_module

def main():
    module = import_module("variable_load_5")
    a = module.a
    print(a)

if __name__ == "__main__":
    main()
