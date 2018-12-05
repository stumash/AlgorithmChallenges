#!/usr/bin/env python3.6

from typing import List, Dict, Deque
from collections import deque
import time

def main():
    t = Terminator()

    start_time = time.time()
    print(sum(1 for _ in (filter(lambda n: t(n) == 89, range(1,10_000_000)))))
    print(f'time (s): {time.time()-start_time}')

class Terminator:
    def __init__(self):
        self.known: Dict[int, int] = {89:89, 1:1}

    def __call__(self, n: int):
        if n in self.known:
            return self.known[n]

        chain: Deque[int] = deque([n])
        while True:
            x = step(chain[-1])

            if x in self.known:
                result = self.known[x]
                for n in chain:
                    self.known[n] = result
                return result

            chain.append(x)

def step(n: int) -> int:
    return sum_of_squares(digits(n))

def digits(n: int) -> List[int]:
    return [int(c) for c in str(n)]

def sum_of_squares(nums: List[int]) -> int:
    return sum(map(lambda x: x*x, nums))

if __name__ == "__main__":
    main()
