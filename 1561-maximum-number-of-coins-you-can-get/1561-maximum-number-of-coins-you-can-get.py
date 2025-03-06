class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        s=0
        print(piles)
        i,j=1,len(piles)-1
        while(i<j):
            s+=piles[i]
            i+=2
            j-=1
        return s


        