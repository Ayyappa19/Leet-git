class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp=[[0 for i in range(len(grid[0]))] for _ in range(len(grid))]

        n=len(grid)
        m=len(grid[0])

        if(len(grid)==1 and 1 in grid[0]):
            return 0
        for i in range(m):
            if(grid[0][i]!=1):
                dp[0][i]=1
            else:
                break
        for i in range(n):
            if(grid[i][0]!=1):
                dp[i][0]=1
            else:
                break
        for i in range(n):
            for j in range(m):
                if(i!=0 and j!=0 and grid[i][j]!=1):
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]

        print(dp)
        return dp[n-1][m-1]

        