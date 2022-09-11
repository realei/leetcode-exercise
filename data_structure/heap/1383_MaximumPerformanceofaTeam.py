from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(speed[i], efficiency[i]) for i in range(n)]
        engineers.sort(key=lambda x: x[1])

        cto, cto_idx = (0, 0), 0
        # Find the best engineer, and title /him/her/them as CTO
        for idx, (s, e) in enumerate(engineers):
            if s*e > cto[0]*cto[1]:
                cto = (s, e)
                cto_idx = idx

        # Eliminate candidates who can't contribute to team

        low_eff = engineers[:cto_idx]
        engineers = engineers[cto_idx+1:]
        engineers.sort(key=lambda x: x[0])

        max_p = cto[0]*cto[1]
        k = k - 1
        while k and engineers:
            k -= 1
            s, e = engineers.pop()
            max_p += s * cto[1]

        print(max_p)

        if k:
            sum_power = sum([e[0] for e in engineers]) + cto[0]
            low_eff.sort(key=lambda x: x[1])
            while k and low_eff:
                k -= 1
                s, e = low_eff.pop()
                sum_power += s
                max_p = max(max_p, sum_power*e)

        return max_p % (10**9 + 7)
