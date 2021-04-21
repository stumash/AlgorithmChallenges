from typing import List


m = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        product = None
        for d in digits:
            assert(d in m.keys())
            if product is None:
                product = m[d]
            else:
                product = [
                    s1 + s2
                    for s1 in product
                    for s2 in m[d]
                ]
        return [] if product is None else product


print(Solution().letterCombinations('234'))
