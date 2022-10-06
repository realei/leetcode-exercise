from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = Counter()
        for c_domain in cpdomains:
            cnt, domain = c_domain.split()
            cnt = int(cnt)
            res[domain] += cnt

            while '.' in domain:
                domain = domain[domain.index('.') + 1:]
                res[domain] += cnt

        return [f"{c} {d}" for d, c in res.items()]
