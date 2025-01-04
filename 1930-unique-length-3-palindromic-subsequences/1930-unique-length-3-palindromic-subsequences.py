class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for k in string.ascii_lowercase:
            f, l = s.find(k), s.rfind(k)
            if f > -1:
                res += len(set(s[f + 1: l]))
        return res