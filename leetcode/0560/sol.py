from typing import List
from collections import defaultdict

class Solution:
  # O(n^2) time & O(n) space, too slow
  def subarraySum(self, nums: List[int], k: int) -> int:
    sums, count = [], 0
    for num in nums:
      sums.append(0)
      for i in range(len(sums)):
        if num + sums[i] == k:
          count += 1
        sums[i] += num
    return count


  # O(n^2) time & O(1) space, still too slow
  def subarraySumFaster(self, nums, k):
    count = 0
    for i,n in enumerate(nums):
      sum = 0
      for j in range(i, len(nums)):
        sum += nums[j]
        if sum == k:
          count += 1
    return count

  # O(n) time & O(n) space
  def subarraySumFastest(self, nums, k):
    sum, count = 0, 0
    d = defaultdict(int, [(0, 1)])

    for num in nums:
      sum += num
      count += d[sum - k]
      d[sum] += 1

    return count

if __name__ == "__main__":
  sol = Solution()
  tests = [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
    ([-1,-1,-1], 0, 0),
    ([-1,-1,1], 0, 1),
    ([1], 0, 0),
  ]
  for nums, k, expected in tests:
    actual = sol.subarraySumFastest(nums, k)
    if actual != expected:
      print(f'nums:{nums}\nk:{k}\nactual:{actual} expected:{expected}\n')

