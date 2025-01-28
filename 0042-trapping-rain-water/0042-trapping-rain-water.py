class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=[0]*n
        r=[0]*n
        ans=0
        for i in range(1,n):
            l[i]=max(l[i-1],height[i-1])
        for j in range(n-2,-1,-1):
            r[j]=max(r[j+1],height[j+1])
            # print(r[j+1],height[j+1])
        print(l,r)
        for i in range(n):
            w=min(l[i],r[i])
            if(w>=height[i]):
                ans+=w-height[i]
        return ans

        