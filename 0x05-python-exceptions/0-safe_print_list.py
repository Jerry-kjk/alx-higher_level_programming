#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for n in range(x):
            print("{:d}".format(my_list[n]), end='')
            num += 1
        print()
        return (num)
    except IndexError:
        print()
        return (num)
