#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0

    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(my_list[i]), end='')
                length += 1
    except IndexError:
        raise

    print()
    return length
