from bisect import bisect_left
from functools import lru_cache
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n=len(endTime)
        start=[job[0] for job in jobs]
        @lru_cache(None)
        def solve(i):
            if i>=n:
                return 0
            nxt_job=bisect_left(start,jobs[i][1])
            # j=i+1
            # while j<n:
            #     if end<=jobs[j][0]:
            #         break
            #     j+=1
            take=jobs[i][2]+solve(nxt_job)
            skp=solve(i+1)
            return max(take,skp)
        return solve(0)