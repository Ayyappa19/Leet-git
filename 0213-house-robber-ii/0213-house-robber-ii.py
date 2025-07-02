class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def rober(l):
            n=len(l)
            if n==0:
                return 0
            elif n==1:
                return l[0]
            dp=[0 for _ in range(n)]
            dp[0]=l[0]
            dp[1]=max(l[0],l[1])
            for i in range(2,n):
                dp[i]=max(dp[i-2]+l[i],dp[i-1])
            return dp[n-1]
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        k=rober(nums[1:])
        x=rober(nums[:n-1])
        return max(k,x)
        