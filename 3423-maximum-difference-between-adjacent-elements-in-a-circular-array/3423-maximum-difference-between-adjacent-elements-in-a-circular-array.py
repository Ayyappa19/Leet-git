class Solution:
    def maxAdjacentDistance(self, l: List[int]) -> int:
        k=abs(l[-1]-l[0])
        for i in range(len(l)-1):
            k=max(k,abs(l[i]-l[i+1]))
        return k

        