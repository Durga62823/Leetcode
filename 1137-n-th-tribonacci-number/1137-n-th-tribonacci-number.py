class Solution:
    def tribonacci(self, n: int) -> int:

        def function(n,dp):
            if n<1:
                return 0
            if n==1 or n==2:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]= function(n-1,dp)+function(n-3,dp)+function(n-2,dp)
            return dp[n]
        dp=[-1]*(n+1)
        return function(n,dp)