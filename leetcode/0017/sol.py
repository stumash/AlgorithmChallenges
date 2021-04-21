from typing import List

def mult(self, ss1: List[str], ss2: List[str]) -> List[str]:
    return [
        s1 + s2
        for s1 in ss1
        for s2 in ss2
    ]

def reduce(xs, f):
    result = None
    for x in xs:
        if result is None:
            result = x
        else:
            result = f(result, x)
    return result if result is not Non

self.m = {
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
            assert(d in self.m.keys())
            if product is None:
                product = self.m[d]
            else:
                product = mult(product, self.m[d])
        return [] if product is None else product


print(Solution().letterCombinations('234'))
