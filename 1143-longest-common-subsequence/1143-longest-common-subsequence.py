class Solution:
    def longestCommonSubsequence(self, s: str, s1: str) -> int:
        n=len(s)
        m=len(s1)
        dp=[[ 0 for i in range(m+1)]for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(s[i-1]==s1[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # print(dp)
        return dp[n][m]

        