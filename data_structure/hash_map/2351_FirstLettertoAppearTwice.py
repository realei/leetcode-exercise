class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char not in seen:
                seen.update({char})
            else:
                return char
