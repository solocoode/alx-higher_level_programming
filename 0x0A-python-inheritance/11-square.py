#!/usr/bin/python3

"""Define Square subclass inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with Rectangle inheritance.

    Attributes:
        __size (int): Size of the square.
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size