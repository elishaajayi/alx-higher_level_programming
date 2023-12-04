#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1

    while i >= 0:
        number = my_list[i]
        print("{:d}".format(number))
        i -= 1
