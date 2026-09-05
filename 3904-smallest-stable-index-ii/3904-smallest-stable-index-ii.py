class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        l=float("inf")
        arr=[0]*n
        for i in range(n-1,-1,-1):
            l=min(l,nums[i])
            arr[i]=l
        r=float('-inf')
        for i in range(n):
            
            r=max(r,nums[i])
            l=arr[i]

            
            if r-l<=k:
                return i
        return -1