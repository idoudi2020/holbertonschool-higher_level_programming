#!/usr/bin/python3
"""
add 2 integers a and b
"""


def add_integer(a, b=98):
    """ function that adds two integers
    Args :
        a (int): first number
        b (int): second number = 98
    Return : sum of both values (int)
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)