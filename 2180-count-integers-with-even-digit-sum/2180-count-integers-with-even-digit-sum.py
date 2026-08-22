class Solution:
    def countEven(self, num: int) -> int:
        count=0
        
        for i in range(2,num+1):
            n=str(i)
            res=0
            for j in n:
                res+=int(j)
            if res%2==0:
                count+=1
        return count