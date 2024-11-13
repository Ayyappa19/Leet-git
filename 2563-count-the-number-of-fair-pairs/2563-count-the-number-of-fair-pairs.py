class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        l = r = n - 1
        
        for i in range(n - 1):
            while r>i and nums[i]+nums[r]>upper:
                r-=1

            while l>i and nums[i]+nums[l]>=lower:
                l-=1

            if r > i:
                ans += r-max(l, i)
        
        return ans