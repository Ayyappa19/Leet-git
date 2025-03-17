class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r=sorted(r)
        m=sorted(m)
        r="".join(r)
        m="".join(m)
        # print(r,m)
        if r in m:
            return True
        else:
            return False

        