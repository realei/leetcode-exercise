"""
https://leetcode.com/problems/valid-palindrome/
"""

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(list(filter(lambda x: x not in string.punctuation, s))).replace(' ', '').lower()
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
