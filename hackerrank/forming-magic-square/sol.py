#!/usr/bin/env python3

import os
from itertools import chain

def rotate_square_90(s):
    return [
        [ s[0][2], s[1][2], s[2][2] ],
        [ s[0][1], s[1][1], s[2][1] ],
        [ s[0][0], s[1][0], s[2][0] ]
    ]

def flip_square(s):
    return [
        [ s[0][2], s[0][1], s[0][0] ],
        [ s[1][2], s[1][1], s[1][0] ],
        [ s[2][2], s[2][1], s[2][0] ]
    ]

square0 = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

squares = []
for square in [ square0, flip_square(square0) ]:
    squares.append(square)
    for _ in range(3):
        squares.append(rotate_square_90(squares[-1]))

squares = [
    [ n for row in square for n in row ]
    for square in squares
]

def cost_to_magic_square(s):
    return min(
        sum(abs(a-b) for a,b in zip(s,square))
        for square in squares
    )

if __name__ == '__main__':
    square = [
        int(n)
        for line in range(3)
        for n in input().split(' ')
    ]

    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        f.write(str(cost_to_magic_square(square)))
