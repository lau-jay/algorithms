#!/usr/bin/env python
# encoding: utf-8

def select_sort(l):
    """
    >>> l = [65, 55, 45, 35, 25, 15, 10]
    >>> select_sort(l)
    [10, 15, 25, 35, 45, 55, 65]
    >>> l2 = [65, 55, 55, 35, 25, 15, 10]
    >>> select_sort(l2)
    [10, 15, 25, 35, 55, 55, 65]
    """
    for i in range(len(l)):
        lowest_number_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[lowest_number_index]:
                lowest_number_index = j
        if lowest_number_index != i:
            l[i], l[lowest_number_index] = l[lowest_number_index], l[i]
    return l

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




