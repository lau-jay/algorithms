#!/usr/bin/env python3
"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        cursor = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cursor]:
                cursor += 1
                # 如果后面的都是重复的那么游标会停下来，直到遇到不重复的
                # 利用不重复的覆盖掉重复的值，所以要cursor + 1
                nums[cursor] = nums[i]
        # 最后停下来的游标就是去重后的最后一位
        # 所以要curosr+1去除后面因为前移了,导致有重复的
        # 之所以不能直接在循环里del是因为会有游标和i重叠这种情况
        del nums[cursor + 1:]
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        """
        解法2, 解法二比较利用了异或的原理
        整体而言，解法2的思路更自然
        """
        i = 1
        while i < len(nums):
            if not nums[i] ^ nums[i - 1]:
                del nums[i - 1]
            else:
                i += 1
        return len(nums)
