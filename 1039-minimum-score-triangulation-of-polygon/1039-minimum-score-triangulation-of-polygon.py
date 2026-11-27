class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n=len(values)
        @lru_cache(None)
        def solve(i,j):
            if j-i==1:
                return 0
            ans=float('inf')
            for k in range(i+1,j):
                cur=values[i]*values[k]*values[j]
                total=cur+solve(i,k)+solve(k,j)
                ans=min(ans,total)
            return ans
        return solve(0,n-1)