def doIt(nums: list[int], j: int, t: int) -> bool:

    memo: dict[tuple[int, int], bool] = {}

    def doItRec(i: int, target: int) -> bool:
        if target == 0:
            return True
        if target < 0 or i < 0:
            return False

        key = (i, target)

        if key in memo:
            return memo[key]

        with_me = lambda: doItRec(i-1, target-nums[i])
        without_me = lambda: doItRec(i-1, target)

        memo[key] = with_me() or without_me()
        return memo[key]

    return doItRec(j, t)


class Solution:
    """
    constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
    """

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        return doIt(nums, len(nums)-1, total//2)




examples = [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
]

s = Solution()
for example, ans in examples:
    assert s.canPartition(example) == ans, f"s.canPartition({example}) != {ans=}"
