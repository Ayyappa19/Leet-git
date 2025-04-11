class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        k=[i for i in range(len(s1)) if s1[i]!=s2[i]]
        if len(k) != 2:
            return False
        i,j=k
        return s1[i]==s2[j]and s1[j]==s2[i]