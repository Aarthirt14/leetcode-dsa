class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        
        for i in range(len(nums)):
            prefix[i]=nums[i]+prefix[i-1]

        total_sum=prefix[-1]
        for i in range(len(nums)):
            left_sum=prefix[i-1]
            right_sum=total_sum-prefix[i]
            if i == 0:
                left_sum = 0
            else:
                left_sum = prefix[i - 1]
            if left_sum == right_sum:
                return i
        return -1
        