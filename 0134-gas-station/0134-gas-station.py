class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        k,c=sum(gas),sum(cost)
        if k<c:
            return -1
        ans,d=0,0
        
        for i in range(len(gas)):
            d+=gas[i]-cost[i]
            if d<0:
                ans=i+1
                d=0 
        
        return ans
                