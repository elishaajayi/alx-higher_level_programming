#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()

    for keys in new.keys():
        new[keys] = new[keys] * 2

    return new
