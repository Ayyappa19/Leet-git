class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        dp=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0]=grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i==0 and j!=0):
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif (i!=0 and j==0):
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                elif (i!=0 and j!=0):
                    x=grid[i][j]+dp[i-1][j]
                    x1=grid[i][j]+dp[i][j-1]
                    dp[i][j]=min(x,x1)
            # print(dp)
        print(dp)
        return dp[n-1][m-1]
        