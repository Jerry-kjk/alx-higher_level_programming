#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    i = 0
    n = 0
    for score, weight in my_list:
        i += score * weight
        n += weight
    return (i / n)
