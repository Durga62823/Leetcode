class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        # def solve(i,n,dp):
            
        #     if i>n-1:
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     pick=nums[i]+solve(i+2,n,dp)
        #     not_pick=solve(i+1,n,dp)
        #     dp[i]= max(pick,not_pick)
        #     return dp[i]
        # dp1=[-1]*(n+2)
        # dp2=[-1]*(n+2)
        # return max(solve(0,n-1,dp1),solve(1,n,dp2))
        def solve(i,n):
            dp=[0]*(len(nums)+2)
            for j in range(n,i-1,-1):
                pick=nums[j]+dp[j+2]
                not_pick=dp[j+1]
                dp[j]=max(pick,not_pick)
                
            return dp[i]
        return max(solve(1,n-1),solve(0,n-2))