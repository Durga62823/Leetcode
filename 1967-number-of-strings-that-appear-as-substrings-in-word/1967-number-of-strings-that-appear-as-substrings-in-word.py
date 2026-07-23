class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
  
        arr=[]

        for i in range(len(word)):
            for j in range(i,len(word)):
                arr.append(word[i:j+1])
        count=0
        for ch in patterns:
            if ch in arr:
                count+=1
        return count