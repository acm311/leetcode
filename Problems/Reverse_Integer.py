"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        bits_32 = 2 ** 31
        need_sign = False
        if x < 0:
            x = abs(x)
            need_sign = True
        num_list = list(map(int, str(x)))
        num_list = num_list[::-1]
        num = int(''.join(map(str,num_list)))
        if need_sign:
            num = -num
        if num >= -bits_32 and num <= bits_32 -1:
            return num
        return 0
