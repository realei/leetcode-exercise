class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        d = {c: i for i, c in enumerate(order)}
        for i in range(n - 1):
            pre, cur = words[i], words[i + 1]
            if pre == cur:
                continue

            sub_len = min(len(pre), len(cur))
            for j in range(sub_len):
                if d[pre[j]] < d[cur[j]]:
                    break
                elif d[pre[j]] > d[cur[j]]:
                    return False

            if len(pre) > len(cur) and pre[:sub_len] == cur:
                return False

        return True
