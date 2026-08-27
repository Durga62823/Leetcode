class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        n=len(num)
        
        if n%2==0:
            l=0
            r=n-1
            while l!=r+1:
                l+=1
                r-=1
            return (num[l]+num[r])/2
        else:

            return num[n//2]
