import math

class DatumNotFound(Exception):
    pass

class BSTree:
    def __init__(self):
        self.root = None
    def insert(self, datum):
        if self.root is not None:
            self.root.insert(datum)
        else:
            self.root = BSTNode(datum)
    def get(self, datum):
        return self.root.get(datum) if self.root is not None else None
    def maxDepth(self):
        return self.root.maxDepth() if self.root is not None else None
    def delete(self, datum):
        if self.root is None:
            return False
        try:
            self.root.delete(datum)
            return True
        except DatumNotFound:
            return False

class BSTNode:
    def __init__(self, datum, left=None, right=None, parent=None):
        self.datum = datum
        self.left = left
        self.right = right
        self.parent = parent

    def get(self, datum):
        if self.datum == datum:
            return self
        if datum <= self.datum:
            if self.left is None:
                return None
            else:
                return self.left.get(datum)
        else:
            if self.right is None:
                return None
            else:
                return self.right.get(datum)

    def insert(self, newDatum):
        if newDatum <= self.datum:
            if not self.left:
                self.left = BSTNode(newDatum, parent=self)
            else:
                self.left.insert(newDatum)
        else:
            if not self.right:
                self.right = BSTNode(newDatum, parent=self)
            else:
                self.right.insert(newDatum)

    def delete(self, datum) -> bool:
        if datum == self.datum:
            if self.left is None and self.right is None:
                pass
        elif datum < self.datum:
            if self.left is not None:
                self.left.delete(datum)
            else:
                raise DatumNotFound(f"{str(datum)} not found in tree")
        elif datum > self.datum:
            if self.right is not None:
                self.right.delete(datum)
            else:
                raise DatumNotFound(f"{str(datum)} not found in tree")

    def maxDepth(self, depth=0):
        leftDepth  = depth if self.left  is None else self.left.maxDepth(depth+1)
        rightDepth = depth if self.right is None else self.right.maxDepth(depth+1)
        return max(leftDepth, rightDepth)

def printBST(tree: BSTree):
    printBSTNode(tree.root)

def printBSTNode(root: BSTNode, depth=0, leftNotRight=None):
    s = depth*'  '
    if not root:
        print(s + '*')
        return
    if leftNotRight is not None:
        if leftNotRight:
            s += "< "
        else:
            s += "> "
    s += str(root.datum)
    print(s)
    printBSTNode(root.left, depth=depth+1, leftNotRight=True)
    printBSTNode(root.right, depth=depth+1, leftNotRight=False)

def createBalancedBinaryTree(sortedList):
    if len(sortedList) < 1:
        raise ValueError("cannot build binary tree from empty list")
    root = createBalancedBinaryTree_(sortedList, 0, len(sortedList))
    tree = BSTree()
    tree.root = root
    return tree

def createBalancedBinaryTree_(sortedList, left, right):
    if left >= right:
        return None
    mid = left + (right-left)//2
    root = BSTNode(sortedList[mid])
    root.left = createBalancedBinaryTree_(sortedList, left, mid)
    root.right = createBalancedBinaryTree_(sortedList, mid+1, right)
    return root

def test():
    # test createBalancedBinaryTree and maxDepth
    for n in [7,8,9]:
        tree = createBalancedBinaryTree(list(range(1, n+1)))
        expectedDepth = math.log(n,2)
        assert(math.floor(expectedDepth) <= tree.maxDepth() <= math.ceil(expectedDepth))
