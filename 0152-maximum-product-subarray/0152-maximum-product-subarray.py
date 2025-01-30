class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = float('-inf')
        ans = 1
        for i in  range(len(nums)):
            if(ans < 0):
                maxi = max(maxi, ans)
                ans = 1
            ans *= nums[i]
            maxi = max(maxi, ans)
        return maxi
