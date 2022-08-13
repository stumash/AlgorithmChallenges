from typing import List

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        best_sum, curr_sum = 0, 0
        for x in nums:
            curr_sum = max(0, curr_sum + x)
            best_sum = max(0, curr_sum)
        return best_sum
