class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=sum(nums[:k])
        x=c/k
        for i in range(len(nums)-k):
            c-=nums[i]
            c+=nums[i+k]
            x=max(x,c/k)
        return x