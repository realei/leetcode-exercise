class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break

        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        m, n = 0, 0

        for i in range(len(s)):
            l_even, r_even = self.expandAroundCenter(s, i, i)
            l_odd, r_odd = self.expandAroundCenter(s, i, i+1)

            if r_even - l_even > n - m:
                m, n = l_even, r_even
            if r_odd - l_odd > n - m:
                m, n = l_odd, r_odd

        return s[m:n+1]
