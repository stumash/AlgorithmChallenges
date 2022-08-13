class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def check_balanced(self) -> bool:
        return self.chb() >= 0
    def chb(self, depth = 0) -> int:
        ld = depth if self.left is None else self.left.chb(depth + 1)
        rd = depth if self.right is None else self.right.chb(depth + 1)

        maxd, mind = max(ld, rd), min(ld, rd)

        if abs(maxd - mind) > 1:
            return -1
        else:
            return maxd


t1=Tree(5,
    Tree(2,
        Tree(1)
    ),
    Tree(7,
        Tree(6)
    )
)

print(t1.check_balanced())

t2=Tree(5,
    Tree(2,
    ),
    Tree(7,
        Tree(6)
    )
)

print(t2.check_balanced())

t3=Tree(5,
    None,
    Tree(7,
        Tree(6)
    )
)

print(t3.check_balanced())

print(Tree(1).check_balanced())
