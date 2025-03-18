class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        r=[0]*m
        l=[0]*n
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(l[i]<grid[i][j]):
                    l[i]=grid[i][j]
                if(r[j]<grid[i][j]):
                    r[j]=grid[i][j]
        # print(l,r)
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                k=min(l[i],r[j])
                if(k>grid[i][j]):
                    s+=k-grid[i][j]
        return s

        