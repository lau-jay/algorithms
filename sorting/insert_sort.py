#!/usr/bin/env python
# encoding: utf-8

def insert_sort(l):
    """
    >>> l = [65, 55, 45, 35, 25, 15, 10]
    >>> insert_sort(l)
    [10, 15, 25, 35, 45, 55, 65]
    >>> l2 = [65, 55, 55, 35, 25, 15, 10]
    >>> insert_sort(l2)
    [10, 15, 25, 35, 55, 55, 65]
    """
    for i in range(1, len(l)):
        position = i
        temp = l[i]
        while position > 0 and l[position - 1] > temp:
            l[position] = l[position - 1]
            position = position - 1
        l[position] = temp
    return l

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




