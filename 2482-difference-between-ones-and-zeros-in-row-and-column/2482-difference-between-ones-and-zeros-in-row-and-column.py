class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n,m=len(grid),len(grid[0])
        r=[0]*n
        c=[0]*m
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    r[i]+=1
                    c[j]+=1
                else:
                    r[i]-=1
                    c[j]-=1
        for i in range(n):
            for j in range(m):
                grid[i][j]=r[i]+c[j]
        return grid


            
                

        