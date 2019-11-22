#!/usr/bin/env python3

import os

def utopian_tree(n):
    height = 1
    for _ in range(n):
        height = height << 1 if height & 1 else height + 1
    return height

if __name__ == '__main__':
    t = int(input())
    periods = [int(input()) for _ in range(t)]
    results = list(map(str, map(utopian_tree, periods)))

    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        f.write("\n".join(results))
