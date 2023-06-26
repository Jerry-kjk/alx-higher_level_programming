#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for n in range(x):
            if type(my_list[n]) is int:
                print("{:d}".format(my_list[n]), end="")
                num += 1
    except (ValueError, TypeError):
        pass
    print()
    return (num)
