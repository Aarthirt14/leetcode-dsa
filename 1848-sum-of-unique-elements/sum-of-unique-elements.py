class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=0
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for key,value in freq.items():
            if value==1:
                count+=key
        return count
        