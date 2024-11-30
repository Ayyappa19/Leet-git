class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))
        x.reverse()
        k=""
        f=0
        for i in x:
            if(i!="-"):
                k+=i
            else:
                f=1
        k=int(k)
        if(k>(2**31)-1):
            return 0
        if(f==0):
            return k
        else:
            return -k