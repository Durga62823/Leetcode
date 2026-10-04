class Solution:
    def checkValidString(self, s: str) -> bool:
        # l=s.count("(")
        # r=s.count(")")
        # e=s.count("*")
        # print(l,r)
        # if l==r:
        #     return True
        # elif l+e==r or r+e==l:
        #     return True
        # else:
        #     return False
        low,high=0,0
        for ch in s:
            if ch=="(":
                low+=1
                high+=1
            elif ch==")":
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            low=max(0,low)
            if high<0:
                return False
        return low==0