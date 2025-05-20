class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        d={}
        if len(p)!=len(s.split(" ")):
            return False
        for i in range(len(p)):
            if p[i] in d:
                if s.split(" ")[i]!=d[p[i]]:
                    return False
            else:
                if s.split(" ")[i] in d.values():
                    return False
                else:
                    d[p[i]]=s.split(" ")[i]
        return True