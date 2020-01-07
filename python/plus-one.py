# -*- coding: utf-8 -*-
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""
from tyeing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        取巧的解法
        :type digits: List[int]
        :rtype: List[int]


        >>> digits = [4,3,2,1]
        >>> digits2 = [1,9,9,9,9]
        >>> s = Solution()
        >>> s.plusOne(digits)
        [4, 3, 2, 2]
        >>> s.plusOne(digits2)
        [2, 0, 0, 0, 0]


        """
        s = int(''.join([str(i) for i in digits]))
        s += 1
        digits = [int(i) for i in str(s)]
        return digits

    def recursive(self, digits: List[int], cursor, plus):
        if plus == 0:
            return
        if cursor < 0:
            digits.insert(0, 1)
            return
        temp = digits[cursor]
        digits[cursor] = (temp + plus) % 10
        plus = (temp + plus) // 10
        self.recursive(digits, cursor - 1, plus)

    def plusOne2(self, digits: List[int]) -> List[int]:
        """
        递归解法
        """
        self.recursive(digits, len(digits) - 1, 1)
        return digits


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
