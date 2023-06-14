#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(a_dictionary.values())
        for i, j in a_dictionary.items():
            if j == max_score:
                return (i)
        return (None)
