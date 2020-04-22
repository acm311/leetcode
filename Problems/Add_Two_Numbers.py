"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)
        result = str(num1 + num2)
        print(result)

    def getNumber(self, list_num: ListNode):
        num1 = ''
        n_list = list_num
        while (n_list != None):
            num1 += str(n_list.val)
            n_list = n_list.next
        return int(num1[::-1])