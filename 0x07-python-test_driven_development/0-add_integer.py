#!/usr/bin/python3
"""Module containing a function for testing"""


def add_integer(a, b=98):
    """Adds two integers, ensuring they are integers or castable to integers.

    Args:
        a (int or float): The first number to add.
        b (int, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
