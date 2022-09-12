from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        max_score, score = 0, 0

        while tokens and (power >= tokens[0] or score):
            while tokens and power >= tokens[0]:
                score += 1
                power -= tokens.pop(0)

            max_score = max(max_score, score)

            if tokens and score:
                score -= 1
                power += tokens.pop()

        return max_score
