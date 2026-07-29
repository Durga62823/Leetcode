class Solution:
    def climbStairs(self, n: int) -> int:
        # def function(n,dp):
        #     if n<=2:
        #         return n
        #     if dp[n]!=-1:
        #         return dp[n]
        #     dp[n]=function(n-1,dp)+function(n-2,dp)
        #     return dp[n]
        # dp=[-1]*(n+1)
        # return function(n,dp)
        dp=[-1]*(n+1)
        if n<=2:
            return n
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[i]
