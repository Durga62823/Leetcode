class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        new=sorted(heights)
        for i in range(len(new)):
            if new[i]!=heights[i]:
                count+=1
        return count