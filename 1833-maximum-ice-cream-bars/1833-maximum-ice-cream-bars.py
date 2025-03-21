class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        k=coins
        c=0
        i=0
        while(k>0 and i<len(costs)):
            if(k<costs[i]):
                return c
            if(k>=costs[i]):
                c+=1
                # print(costs[i])
                k-=costs[i]
                # print(k)
            
            i+=1
        return c
        