class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def solve(i,n,dp):
            
            if i>n-1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick=nums[i]+solve(i+2,n,dp)
            not_pick=solve(i+1,n,dp)
            dp[i]= max(pick,not_pick)
            return dp[i]
        dp1=[-1]*(n+2)
        dp2=[-1]*(n+2)
        return max(solve(0,n-1,dp1),solve(1,n,dp2))