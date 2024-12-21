class Solution:
    def climbStairs(self, n: int) -> int:
        d=[0 for i in range(n+1)]
        
        d[0]=1
        d[1]=1
        print(d)
        for i in range(2,n+1):
            d[i]=d[i-1]+d[i-2]
            # print(i)
        # print(d)
        return d[n]
        
        