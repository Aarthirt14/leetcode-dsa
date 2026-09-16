class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output=[]
        frequency={}
        for x in nums:
            frequency[x]=frequency.get(x,0)+1
        for x, count in frequency.items():
            if count > 1:
                output.append(x)

        return output