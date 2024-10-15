class Solution:
    def minimumSteps(self, s: str) -> int:
        c, x= 0, 0
        for i in s:
            if i=='1':
                x+=1
            else:
                c+=x
        return c     
        