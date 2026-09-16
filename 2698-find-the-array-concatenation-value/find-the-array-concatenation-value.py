class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        value=0
        first=0
        last=len(nums)-1
        if len(nums)==1:
            return 1
        while first < last :
            concatenate=str(nums[first])+str(nums[last])
            value+=int(concatenate)
            first+=1
            last-=1
            if first==last:
                value+=nums[first]
        return value



        