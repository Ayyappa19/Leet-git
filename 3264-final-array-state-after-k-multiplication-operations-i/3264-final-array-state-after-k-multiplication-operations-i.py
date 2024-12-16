class Solution:
    def getFinalState(self, nums: List[int], k: int, mu: int) -> List[int]:
        for i in range(k):
            
            x=min(nums)
            y=nums.index(x)
            nums[y]*=mu
          
        return nums      # break