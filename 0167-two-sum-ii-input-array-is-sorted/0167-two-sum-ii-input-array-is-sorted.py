class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]
        mpp={}
        for i in range(len(numbers)):
            mpp[numbers[i]]=i+1
        for i in range(len(numbers)):
            cur=numbers[i]
            req=target-cur
            if req in mpp:
                return [i+1,mpp[req]]