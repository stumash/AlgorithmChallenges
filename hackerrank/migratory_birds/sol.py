from typing import List
from collections import defaultdict

def sol(arr: List[int]) -> int:
    d = defaultdict(int)
    for a in arr:
        d[a] += 1
    most_viewings = max(d.values())
    return min(a for a in d if d[a] == most_viewings)

input()
print(sol(list(map(int, input().split(' '))))
