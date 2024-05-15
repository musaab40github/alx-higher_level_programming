#!/usr/bin/python3

if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    if add:
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sub:
        print("{} - {} = {}".format(a, b, sub(a,b)))
    elif mul:
        print("{} * {} = {}".format(a, b, mul(a,b)))
    else:
        print("{} / {} = {}".format(a, b, div(a,b)))
