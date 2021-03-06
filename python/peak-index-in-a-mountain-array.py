# -*- coding: utf-8 -*-
"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

1. 3 <= A.length <= 10000
2. 0 <= A[i] <= 10^6
3. A is a mountain, as defined above.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        mountain_index = 0
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i]:
                mountain_index = i
        return mountain_index

    def peakIndexInMountainArray2(self, A: List[int]) -> int:
        i, j = 0, len(A) - 1
        while i < j:
            mid = (i + j) // 2

            if A[mid] > A[(mid + 1)]:
                j = mid
            else:
                i = mid + 1
        return i
