class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n=len(word1)
        m=len(word2)
        rsidematch=[0]*(n)
        rmatch=0
        i=n-1
        j=m-1
        while i>=0:
            if j>=0 and word1[i]==word2[j]:
                rmatch+=1
                j-=1
            rsidematch[i]=rmatch
            i-=1
        i,j=0,0
        canchange=True
        res=[]
        while i<n and j<m:
            if word1[i]==word2[j]:
                res.append(i)
                j+=1
            elif canchange and i+1<n and rsidematch[i+1]>=m-j-1:
                canchange=False
                res.append(i)
                j+=1

            
            i+=1
        return res if j==m else []
