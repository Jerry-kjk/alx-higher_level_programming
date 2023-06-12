#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
       is_divisible = (n % 2 == 0)
       new_list.append(is_divisible)
    return (new_list)
