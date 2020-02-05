#!/usr/bin/env python3

def deforestation(n, tree):
    return None

def printTree(tree, depth=0):
    for k in tree:
        print("  "*depth + str(k))
        printTree(tree[k], depth+1)

if __name__ == "__main__":
    for _ in range(int(input())):
        tree = {1: {}}
        nodes = {1: tree[1]}

        n = int(input())
        for _ in range(n-1):
            u, v = tuple(map(int, input().split(' ')))
            existing, toAdd = (u,v) if u in nodes else (v,u)

            nodes[existing][toAdd] = {}
            nodes[toAdd] = nodes[existing][toAdd]

        printTree(tree)

        result = deforestation(n, tree)
        print("Alice" if result else "Bob")
