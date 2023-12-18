#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0

    # Find number of elements in list
    while my_list:
        try:
            test = my_list[length]
            length += 1
        except IndexError:
            break
    if x > length:
        for element in my_list:
            print("{:d}".format(element), end='')
        print("")
        return (length)
    else:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
        print("")
        return (x)
