class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        """
        if len(s) != len(t):
            return False
        
        st_dict, ts_dict = {}, {}
        
        for i in range(len(s)):
            if s[i] not in st_dict.keys():
                st_dict[s[i]] = t[i]
            else:
                if st_dict[s[i]] != t[i]:
                    return False

            if t[i] not in ts_dict.keys():
                ts_dict[t[i]] = s[i]
            else:
                if ts_dict[t[i]] != s[i]:
                    return False

        return True
