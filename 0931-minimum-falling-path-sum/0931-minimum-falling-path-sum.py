class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]
        n = len(matrix)
        dp = matrix.copy() 
        for i in range(n-2,-1,-1):
            for j in range(n):
                d = dp[i+1][j]
                if(j>0):
                    d = min(d,dp[i+1][j-1])
                if(j<n-1):
                    d = min(d,dp[i+1][j+1])
                dp[i][j] += d

        result = float('inf')
        print(dp)
        for num in dp[0]:
            result = min(result, num)
        return result