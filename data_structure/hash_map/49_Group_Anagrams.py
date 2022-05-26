from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for st in strs:
            counts = [0]*26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
                
            # key of `hash table` only accept `immutable datatype`
            # `immutable datatype`: string, tuple, number
            # `mutable datatype`: list, set, dict
            mp[tuple(counts)].append(st)
            
        return list(mp.values())
