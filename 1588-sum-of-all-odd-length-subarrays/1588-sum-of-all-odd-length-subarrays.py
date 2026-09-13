class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (j-i+1)%2!=0:
                    count+=sum(arr[i:j+1])
                    print(count)
        return count