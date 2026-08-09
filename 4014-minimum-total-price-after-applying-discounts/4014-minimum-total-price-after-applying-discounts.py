class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        print(prices)
        n=len(prices)
        m=len(discounts)
        i,j=0,0
        res=0
        while i<n:
            
            res+=prices[i]*(100-discounts[j])/100
            print(res)
            i+=1
            j+=1
            if j==m:
                while i<n:
                    res+=prices[i]
                    i+=1
        return res
            