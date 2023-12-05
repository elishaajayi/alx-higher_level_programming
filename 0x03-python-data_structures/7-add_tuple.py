#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)

    for i in range(2):
        result.append(tuple_a[i] + tuple_b[i])

    result = tuple(result)
    return (result)
