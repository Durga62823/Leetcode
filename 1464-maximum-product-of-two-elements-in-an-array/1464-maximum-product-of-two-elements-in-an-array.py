class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=float('-inf')
        i=0
        while i<len(nums):
            for j in range(i+1,len(nums)):
                val=(nums[i]-1)*(nums[j]-1)
                res=max(res,val)
            i+=1
        return res
