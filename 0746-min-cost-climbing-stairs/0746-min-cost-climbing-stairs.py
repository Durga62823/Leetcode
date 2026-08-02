class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def function(i,dp):
        #     if i>=len(cost):
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     dp[i]= cost[i]+min(function(i+1,dp),function(i+2,dp))
        #     return dp[i]
        n=len(cost)
        dp=[-1]*(n+2)
        # return min(function(0,dp),function(1,dp))
        
        dp[n]=0
        dp[n+1]=0
        for i in range(n-1,-1,-1):
            dp[i]=cost[i]+min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])