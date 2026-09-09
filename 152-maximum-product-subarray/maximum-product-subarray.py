class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max=nums[0]
        current_min=nums[0]
        best=nums[0]

        for i in range(1,len(nums)):
            num=nums[i]
            old_max = current_max
            old_min = current_min
            current_max=max(nums[i],current_max*nums[i],old_min*num)
            current_min=min(nums[i],current_min*nums[i],old_max*num)
            best=max(current_max,best)

        return best
        