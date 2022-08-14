from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        cnt = Counter(text)
        cnt_bal = Counter('balloon')

        return min([cnt[c] // cnt_bal[c] for c in cnt_bal])
