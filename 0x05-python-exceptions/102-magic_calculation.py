#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for n in range(1, 4):
        try:
            if n > a:
                raise Exception('Too far')
            result += (a ** b) / n
        except:
            result = b + a
            break
    return (result)
