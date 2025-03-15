class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        c=1
        if(len(nums)==0):
            return 0
        for i in range(len(nums)-1):
            if (nums[i]+1 == nums[i+1]):
                c+=1 
            elif(nums[i]==nums[i+1]):
                continue
            elif(nums[i]+1 !=nums[i+1]):
                c=1
            m=max(c,m)
        m=max(c,m)

        print(nums)
        return m
            
        