#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            if self.area() == other.area():
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Square):
            if self.area() != other.area():
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Square):
            if self.area() > other.area():
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Square):
            if self.area() >= other.area():
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Square):
            if self.area() < other.area():
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Square):
            if self.area() <= other.area():
                return True
            else:
                return False
        else:
            return False
