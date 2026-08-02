class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def function(i,dp):
            if i>=len(cost):
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]= cost[i]+min(function(i+1,dp),function(i+2,dp))
            return dp[i]
        dp=[-1]*(len(cost))
        return min(function(0,dp),function(1,dp))