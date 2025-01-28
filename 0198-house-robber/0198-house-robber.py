class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0 for i in range(len(nums)+1)]
        if(len(nums)<=2):
            return max(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        n=len(nums)
        for i in range(2,len(nums)):
            m=0
            for j in range(i-1):
                m=max(dp[j],m)
            dp[i]=m+nums[i]
        print(dp)
        return (max(dp[n-1],dp[n-2]))


            
        