#!/usr/bin/python3

"""Class MyList that inherits from list."""


class MyList(list):
    """List with sorted printing."""

    def print_sorted(self):
        """Print a list in sorted order."""
        print(sorted(self))
