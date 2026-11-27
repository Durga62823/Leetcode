class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts.sort()
        cuts=[0]+cuts+[n]
        m=len(cuts)
        @lru_cache(None)
        def solve(i,j):
            if j-i==1:
                return 0
            ans=float('inf')
            for k in range(i+1,j):
                cur=(cuts[j]-cuts[i])+solve(i,k)+solve(k,j)
                ans=min(cur,ans)
            return ans

        return solve(0,m-1)