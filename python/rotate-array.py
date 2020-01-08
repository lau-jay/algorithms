# -*- coding: utf-8 -*-
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

"""
from typing import List


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        >>> s = Solution()
        >>> test1, k1 = [-1,-100,3,99],2
        >>> test2, k2 = [1],0
        >>> test3, k3 = [1,2,3,4,5], 1
        >>> test4, k4 = [1,2], 3
        >>> s.rotate(test1, k1)
        >>> print(test1)
        [3, 99, -1, -100]
        >>> s.rotate(test2, k2)
        >>> print(test2)
        [1]
        >>> s.rotate(test3, k3)
        >>> print(test3)
        [5, 1, 2, 3, 4]
        >>> s.rotate(test4, k4)
        >>> print(test4)
        [2, 1]
        """
        if not k:
            return
        # 边界条件, k可能比数组长度还大
        k = k % len(nums)
        temp = nums[-k:]
        nums[k:] = nums[0:-k]
        nums[0:k] = temp

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        解法2, 通用
        >>> s = Solution()
        >>> test1, k1 = [-1,-100,3,99],2
        >>> test2, k2 = [1],0
        >>> test3, k3 = [1,2,3,4,5], 1
        >>> test4, k4 = [1,2], 3
        >>> s.rotate2(test1, k1)
        >>> print(test1)
        [3, 99, -1, -100]
        >>> s.rotate2(test2, k2)
        >>> print(test2)
        [1]
        >>> s.rotate2(test3, k3)
        >>> print(test3)
        [5, 1, 2, 3, 4]
        >>> s.rotate2(test4, k4)
        >>> print(test4)
        [2, 1]
        """
        if not k:
            return
        # 边界条件, k可能比数组长度还大
        k = k % len(nums)
        # 0 to  len(nums) - 1- k
        i, j = 0, len(nums) - 1 - k
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # k+1 to end (len(nums) - 1)
        i, j = len(nums) - k, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # reverse
        i, j = 0, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
