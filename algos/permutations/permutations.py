from functools import lru_cache

def permutations(xs):
    if len(xs) == 1:
        return [xs]

    return [
        [xs[i]] +  p
        for i in range(len(xs))
        for p in permutations(xs[:i]+xs[i+1:])
    ]
