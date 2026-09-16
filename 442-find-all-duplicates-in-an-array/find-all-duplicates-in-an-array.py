class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output=[]
        frequency={}
        for x in nums:
            frequency[x]=frequency.get(x,0)+1
        for x in nums:
            if frequency[x] > 1 :
                output.append(x)
        output= set(output)
        return list(output)