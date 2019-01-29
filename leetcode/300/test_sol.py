from sol import Solution

soln = Solution()

def test_dp_lengthOfLIS():
    nums = [10,9,2,5,3,7,101,18]
    assert(4 == soln.dp_lengthOfLIS(nums))

def test_dp_lengthOfLIS_bottom_up():
    nums = [10,9,2,5,3,7,101,18]
    assert(4 == soln.dp_lengthOfLIS_bottom_up(nums))

def test_dp_lengthOfLIS_2D_bottom_up():
    nums = [10,9,2,5,3,7,101,18]
    assert(4 == soln.dp_lengthOfLIS_2D_bottom_up(nums))
