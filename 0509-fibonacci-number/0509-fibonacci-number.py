class Solution:
    def fib(self, n: int) -> int:
        # p=[-1]*(n+1)
        # def dp(i,p):
        #     if i<=1:
        #         return i
        #     if p[i]!=-1:
        #         return p[i]
        #     p[i]=dp(i-1,p)+dp(i-2,p)
        #     return p[i]
        # return dp(n,p)
        if n<2:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[i]