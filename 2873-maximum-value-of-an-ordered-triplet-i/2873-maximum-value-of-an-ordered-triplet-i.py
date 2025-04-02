class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        m,k,ans=nums[0], 0, 0
        for i in range(1, n-1):
            k=max(k,m-nums[i])
            m=max(m,nums[i])
            ans=max(ans,k*nums[i+1])
        return ans
        