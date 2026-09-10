class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            previous_prefix = prefix_sum - k

            if previous_prefix in freq:
                count += freq[previous_prefix]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
        
        
        
        


        