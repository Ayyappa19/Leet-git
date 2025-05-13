class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=[]
        li,h=0,0
        for i in range(len(nums)):
            if i!=len(nums)-1 and nums[i]+1==nums[i+1]:
                h+=1
            else:
                k=""
                if li!=h:
                    k+=str(nums[li])
                    k+="->"
                    k+=str(nums[h])
                else:
                    k+=str(nums[li])
                l.append(k)
                h+=1
                li=h
        return l
                    
        