from typing import List

def is_valid(queens):
    for i1,j1 in list(enumerate(queens)):
        for i2,j2 in list(enumerate(queens[:i1])):
            if j1 == j2 or (j1-i1) == (j2-i2) or (i1+j1) == (i2+j2):
                return False
    return True

def n_queens(N, i=None) -> List[List[int]]:
    if i is None:
        i = N
    if i <= 1:
        return [[j] for j in range(N)]
    results = []
    for r in n_queens(N, i-1):
        for i in range(N):
            curr = r + [i]
            if is_valid(curr):
                results.append(curr)
    return results

assert(len(n_queens(1)) == 1)
assert(len(n_queens(2)) == 0)
assert(len(n_queens(3)) == 0)
assert(len(n_queens(4)) == 2)
assert(len(n_queens(5)) == 10)
# print(n_queens(6))
# print(n_queens(7))
assert(len(n_queens(8)) == 92)
assert(len(n_queens(9)) == 352)
# assert(len(n_queens(10)) == 724)
# assert(len(n_queens(11)) == 2680)
# assert(len(n_queens(12)) == 14200) # too slow
# assert(len(n_queens(13)) == 73172) # too slow


def n_queens_fast():
    pass
