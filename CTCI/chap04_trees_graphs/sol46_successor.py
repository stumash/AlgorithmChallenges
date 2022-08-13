from typing import Optional

class Tree:
    def __init__(self,
        value,
        parent: Optional['Tree']=None,
        left: Optional['Tree']=None,
        right: Optional['Tree']=None
    ):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def succ(self) -> Optional['Tree']:
        if self.right is not None:
            curr, next = self.right, self.right.left
            while next:
                curr = next
                next = curr.left
            return curr
        else:
            return self.parent

x = Tree(5)
xl = Tree(2, x); x.left = xl
xr = Tree(7, x); x.right = xr

assert(xl.succ() == x)
assert(x.succ() == xr)
assert(xr.succ() == None)


x = Tree(5)
xl = Tree(2, x); x.left = xl
xr = Tree(7, x); x.right = xr
