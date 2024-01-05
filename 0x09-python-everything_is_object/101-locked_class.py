#!/usr/bin/python3
"""Class to define a locked class"""


class LockedClass:
    """
    The class only only allows the instantiating of first_name attributes
    """

    __slots__ = ['first_name']
