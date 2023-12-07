#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    checked = []
    count = 0

    for num in my_list:
        count = 0
        for check in checked:
            if num == check:
                count += 1

        if count == 0:
            sum = sum + num
            checked.append(num)

    return sum;
