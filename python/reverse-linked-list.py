# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            after = current.next  # 保存当前的下一个
            current.next = prev  # 反转
            prev = current  # prev指针后移， 所以最后prev是头结点了
            current = after
        return prev
