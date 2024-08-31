class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums)

        s = []
        ans = []

        for i in range(len(nums)-1,-1,-1):

            while len(s)>0 and s[len(s)-1]<=nums[i]:
                s.pop()

            if len(s)==0:
                ans.append(-1)

            else:
                ans.append(s[len(s)-1])

            s.append(nums[i])

        ans = ans[::-1]
        return ans[:n]