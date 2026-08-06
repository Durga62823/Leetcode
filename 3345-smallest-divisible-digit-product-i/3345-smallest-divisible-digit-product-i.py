class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i=n
        while i>=n:
            ch=str(i)
            val=1
            for j in ch:
                val*=int(j)
            if val%t==0:
                return i
            else:
                i+=1
        