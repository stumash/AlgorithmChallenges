from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        result = 1
        for n in nums:
            s.add(n)
            while result in s:
                result += 1
        return result

    def firstMissingPositiveFastest(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        for n in nums:
            while n >= 0 and n < len(nums):
                temp = nums[n]
                nums[n] = n
                if temp == n:
                    break
                n = temp
        result = 1
        for i,n in enumerate(nums):
            if i == 0: continue
            if n != result:
                break
            result += 1
        return result

if __name__ == "__main__":
    tests = [
        ([2,1], 3),
        ([1], 2),
        ([1,2,0], 3),
        ([3,4,-1,1], 2),
        ([7,8,9,11,12], 1),
    ]
    for nums, expected in tests:
        actual = Solution().firstMissingPositive(nums)
        if actual != expected:
            print(f'expected {expected}, got {actual} for firstMissingPositive({nums})')

        numsc = nums[:]
        actual = Solution().firstMissingPositiveFastest(nums)
        if actual != expected:
            print(f'Fastest: expected {expected}, got {actual} for firstMissingPositive({numsc})')
