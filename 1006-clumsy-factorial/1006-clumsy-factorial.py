class Solution:
    def clumsy(self, n: int) -> int:
        s=['*','//','+','-']
        s1=""
        i=0
        while(n>1):
            s1+=str(n)
            s1+=s[i]
            i=(i+1)%4
            n-=1
        s1+=str(n)
        print(s1)
        return int(eval(s1))
            
        