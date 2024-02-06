#!/usr/bin/python3

"""Define a function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Add attribute to object if possible.

    Args:
        obj (any): Object to add attribute to.
        att (str): Name of attribute to add.
        value (any): Value of attribute.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute")
    setattr(obj, att, value)