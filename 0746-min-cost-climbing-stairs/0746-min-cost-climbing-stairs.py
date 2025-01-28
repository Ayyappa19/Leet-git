class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.reverse()
        print(cost)
        n=len(cost)
        dp=[0 for i in range(len(cost)+1)]
        dp[n]=cost[n-3]
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        # print(cost)
        return min(cost[0],cost[1])

        