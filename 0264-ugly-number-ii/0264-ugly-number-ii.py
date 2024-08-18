class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l1=set()
        l1.add(1)
        for i in range(1,n+1):
            l1.add(2*i)
            l1.add(3*i)
            l1.add(5*i)
        l=list(l1)
        l.sort()
        return l[n-1]
        