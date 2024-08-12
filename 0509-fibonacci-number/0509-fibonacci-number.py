class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        a,b=0,1
        n-=1
        c=b
        while(n):
            c=a+b
            a=b
            b=c
            n-=1
        return c
        