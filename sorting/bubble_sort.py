#!/usr/bin/env python
# encoding: utf-8

def bubble_sort(l):
    """
    >>> l = [65, 55, 45, 35, 25, 15, 10]
    >>> bubble_sort(l)
    [10, 15, 25, 35, 45, 55, 65]
    >>> l2 = [65, 55, 55, 35, 25, 15, 10]
    >>> bubble_sort(l2)
    [10, 15, 25, 35, 55, 55, 65]
    """
    unsorted_until_index = len(l) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if l[i] > l[i+1]:
                sorted = False
                l[i], l[i+1] = l[i+1], l[i]
        unsorted_until_index = unsorted_until_index - 1
    return l

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




