class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n-2):
            if (nums[i]+nums[i+2])*2==nums[i+1]:
                c+=1 
        return c 
