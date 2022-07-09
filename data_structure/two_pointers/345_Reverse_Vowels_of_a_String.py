class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1

        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"

        s = list(s)

        while left < right:
            if isVowel(s[left]) and isVowel(s[right]):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            if not isVowel(s[left]):
                left += 1
            if not isVowel(s[right]):
                right -= 1

        return "".join(s)
