class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=min(nums)
        l=max(nums)
        res=[]
        for num in range(s,l+1):
            if num not in nums:
                res.append(num)
        return res
    