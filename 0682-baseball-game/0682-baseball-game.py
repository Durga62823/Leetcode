class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res=[]
        for ch in operations:
            if ch=="D":
                res.append(res[-1]*2)
            elif ch=="+":
                res.append(res[-1]+res[-2])
            elif ch=="C":
                    res.pop()

            else:
                
                res.append(int(ch))
        return sum(res)