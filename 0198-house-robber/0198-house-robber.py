class Solution:
    def rob(self, nums: List[int]) -> int:

        # def function(i,nums,dp):
        # #     if i>=len(nums):
        # #         return 0
           
        # #     pick=nums[i]+function(i+2,nums,dp)
        # #     not_pick= function(i+1,nums,dp)
        # #     dp[i]= max(pick,not_pick)
        # #     return dp[i]
        # # dp=[-1]*(len(nums))
        # # return function(0,nums,dp)
        n=len(nums)
        dp=[-1]*(n+2)
        dp[n]=0
        dp[n+1]=0
        for i in range(n-1,-1,-1):
            pick=nums[i]+dp[i+2]
            not_pick=dp[i+1]
            dp[i]=max(pick,not_pick)

        return dp[0]