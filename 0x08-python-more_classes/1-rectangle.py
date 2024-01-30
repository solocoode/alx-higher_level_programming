#!/usr/bin/python3
"""Class defining a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


# Additional test cases
try:
    myrectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    myrectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

myrectangle = Rectangle(2, 4)
print(sorted(myrectangle.__dict__))
print(myrectangle.width)
print(myrectangle.height)

myrectangle = Rectangle(2, 4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
myrectangle.width = 10
print("{} - {}".format(myrectangle.width, myrectangle.height))

myrectangle = Rectangle(2, 4)
print("{} - {}".format(myrectangle.width, myrectangle.height))
myrectangle.height = 10
print("{} - {}".format(myrectangle.width, myrectangle.height))

try:
    myrectangle = Rectangle(2, "3")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    myrectangle = Rectangle("2", 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))