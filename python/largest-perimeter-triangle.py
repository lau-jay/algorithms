#!/usr/bin/env python
# encoding: utf-8

"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:
3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        """
        >>> s = Solution()
        >>> A =  [1,2,1]
        >>> s.largestPerimeter(A)
        0
        >>> A =  [3, 2, 3, 4]
        >>> s.largestPerimeter(A)
        10
        >>> A =  [3, 6, 2, 3]
        >>> s.largestPerimeter(A)
        8
        """
        A.sort(reverse=True)
        max_value = A[0]
        for i in range(1, len(A)-1):
            if max_value >= (A[i] + A[i+1]):
                max_value = A[i]
                continue
            else:
                return sum([max_value, A[i], A[i+1]])
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
