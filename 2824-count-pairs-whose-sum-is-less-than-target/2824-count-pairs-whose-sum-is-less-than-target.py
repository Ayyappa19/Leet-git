class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,j=0,1
        # // -1,1,1,2,3
        # //  i j 
        c=0
        while(i<len(nums)-1):
            j=i+1
            while(j<len(nums)):
                if(nums[i]+nums[j]>=target):
                    break
                else:
                    c+=1
                j+=1
            i+=1
        return c

        