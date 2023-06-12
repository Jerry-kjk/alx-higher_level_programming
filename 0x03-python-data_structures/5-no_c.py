#!/usr/bin/python3
def no_c(my_string):
    updated_str = ''
    for n in my_string:
        if n.lower() != 'c':
            updated_str += n
    return (updated_str)
