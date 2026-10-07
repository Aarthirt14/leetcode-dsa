class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        #count below or equal to upper
        left=0
        right=len(nums)-1
        count1=0
        while left < right:
            if nums[left]+nums[right]<=upper:
                count1+=(right-left)
                left+=1
            else:
                right-=1
        left=0
        right=len(nums)-1
        count2=0
        while left < right:
            if nums[left]+nums[right] < lower:
                count2+=(right-left)
                left+=1
            else:
                right-=1
        return (count1 - count2)
        
            
        