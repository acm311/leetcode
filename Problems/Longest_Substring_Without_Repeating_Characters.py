"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_sub = 0
        while (len(s) > 0):
            len_tmp = self.get_len_subs(s)
            if len_tmp > len_sub:
                len_sub = len_tmp
            s = s[1:]
        return len_sub

    def get_len_subs(self, s):
        subs = ''
        for c in s:
            if c in subs:
                return len(subs)
            else:
                subs = subs + c
        return len(subs)

# option 2
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         len_str = len(s)
#         resp = 0
#
#         for i in range(len_str):
#             for j in range(i, len_str):
#                 sub_str = s[i:j + 1]
#                 if self.all_dif_characters(sub_str) and len(sub_str) > resp:
#                     resp = len(sub_str)
#         return resp
#
#     def all_dif_characters(self, s):
#         my_tuple = set(s)
#         new_s = ''.join(my_tuple)
#         if len(s) == len(new_s):
#             return True
#         return False

