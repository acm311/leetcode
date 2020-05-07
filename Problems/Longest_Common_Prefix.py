"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]

        wd = strs[0]
        prefix_all = False
        while len(wd) > 0:
            for word in strs[1:]:
                if word.startswith(wd):
                    prefix_all = True
                else:
                    prefix_all = False
                    break
            if prefix_all:
                break
            wd = wd[:-1]
        return wd
