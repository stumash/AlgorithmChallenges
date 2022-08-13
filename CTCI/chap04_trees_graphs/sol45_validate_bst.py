class Tree:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def validate_bst(self) -> bool:
        vl = True if self.left is None else self.left.validate_bst()
        vr = True if self.right is None else self.right.validate_bst()

        v = True
        if self.left is not None and self.left.value > self.value:
            v = False
        if self.right is not None and self.right.value < self.value:
            v = False

        return vl and vr and v

t1=Tree(5,
    Tree(2,
        Tree(1)
    ),
    Tree(7,
        Tree(6)
    )
)

print(t1.validate_bst())

t2=Tree(5,
    Tree(2,
    ),
    Tree(7,
        Tree(6)
    )
)

print(t2.validate_bst())

t3=Tree(5,
    None,
    Tree(7,
        Tree(6)
    )
)

print(t3.validate_bst())

print(Tree(1).validate_bst())

t4=Tree(5,
    None,
    Tree(7,
        Tree(8)
    )
)

print(t4.validate_bst())
