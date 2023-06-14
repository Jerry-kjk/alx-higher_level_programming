#!/usr/bin/python3
roman_num = {'I': 1, 'V': 5, 'IX': 9, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def roman_to_int(roman_string):
    x = 0
    if not isinstance(roman_string, str):
        return x
    r_numeral = roman_num.keys()
    n = len(roman_string)
    i = 0
    while i < n:
        result_1 = roman_string[i:i+2]
        result_2 = roman_string[i]
        if result_1 in r_numeral:
            x += roman_num.get(result_1)
            i += 2
        elif result_2 in r_numeral:
            x += roman_num.get(result_2)
            i += 1

    return x
