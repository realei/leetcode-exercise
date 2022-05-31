class Solution:
    L = 10
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        cnt = collections.defaultdict(int)
        for i in range(len(s) - self.L + 1):
            sub = s[i:i+self.L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans
