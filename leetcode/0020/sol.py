class Solution:
    bs = [('(', ')'), ('[', ']'), ('{', '}')]
    opens, closes = zip(*bs)
    c2o = {c:o for c,o in zip(closes, opens)}

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in Solution.opens:
                stack.append(c)
            else:
                if not stack or stack.pop() != Solution.c2o[c]:
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    for test, expected in [
        ("[({}()[])]", True),
        ("[{()[]{[((])]}}]", False),
        ("]", False),
    ]:
        assert(sol.isValid(test) == expected)
