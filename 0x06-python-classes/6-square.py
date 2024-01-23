#!/usr/bin/python3
"""coordinates of a square"""


class Square():
    """A square with its attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """"Initialize the square with specified size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """"get the size of the square"""
        return self.__size

    @property
    def position(self):
        """"get the position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """"set the size with proper validation"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """"set the position"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """"get area of the square"""
        return self.size ** 2

    def my_print(self):
        """print the square using '#' characters"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
