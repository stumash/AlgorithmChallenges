from sol import Solution

soln = Solution()

io_pairs = [
    ( [10,9,2,5,3,7,101,18] , 4 ),
    ( [1,3,6,7,9,4,10,5,6]  , 6 )
]

def test_dp_lengthOfLIS():
    for nums, ans in io_pairs:
        assert(soln.dp_lengthOfLIS(nums) == ans)

def test_dp_lengthOfLIS_bottom_up():
    for nums, ans in io_pairs:
        assert(soln.dp_lengthOfLIS_bottom_up(nums) == ans)
