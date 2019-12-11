from itertools import product

r"""

I have an array of N randomly ordered unique integers 1 to N. I iterate over A and
insert each number into a Binary Search Tree.

I give you the BST.

Give me all possible values of A.

Example:
        2
       / \      Output: [ [2, 1, 3], [2, 3, 1] ]
      1   3

Hint: All you really know is that the parent was inserted before any of its children.
"""

class TreeNode:
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

def all_sequences(root: TreeNode):
    if root is None:
        return [[]]
    return [
        [root.datum] + w
        for seq1,seq2 in product(all_sequences(root.left), all_sequences(root.right))
        for w in all_weaves(seq1, seq2)
    ]

def all_weaves(seq1, seq2, i=0, j=0):
    if i == len(seq1) and j == len(seq2):
        return [ [] ]
    elif i == len(seq1):
        return [ seq2[j:] ]
    elif j == len(seq2):
        return [ seq1[i:] ]
    else:
        return [
            *[[seq1[i]] + w for w in all_weaves(seq1, seq2, i=i+1, j=j)],
            *[[seq2[j]] + w for w in all_weaves(seq1, seq2, i=i, j=j+1)]
        ]

def test():
    root = TreeNode(
        2,
        left=TreeNode(1),
        right=TreeNode(3),
    )
    for p in all_sequences(root):
        print(p)
