from collections import deque
import random

def main():
    shuffled = lambda l: random.sample(l, len(l))
    random_half = lambda l: random.sample(l, len(l)//2)

    nums = shuffled(list(range(1,10+1)))

    tree = AVLTree()

    for num in nums:
        tree.insert(num)
    tree.print()

    print()

    # for num in random_half(nums):
        # tree.remove(num)
    # tree.print()

class AVLTree:
    def __init__(self):
        self.top_root = None

    def insert(self, val):
        self.top_root = self._insert(self.top_root, val)

    def _insert(self, root, val):
        if not root:
            return AVLTreeNode(val)
        elif val <= root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        root.update_height()

        balance_factor = root.balance_factor()

        if balance_factor > 1:
            balance_factor = root.left.balance_factor()
            if balance_factor > 0: # left-left
                return self._rotate_right(root)
            else:                  # left-right
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        elif balance_factor < -1:
            balance_factor = root.right.balance_factor()
            if balance_factor < 0: # right-right
                return self._rotate_left(root)
            else:                  # right-left
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def _rotate_left(self, root):
        old_right = root.right
        new_right = old_right.left

        root.right = new_right
        old_right.left = root

        root.update_height()
        old_right.update_height()

        return old_right

    def _rotate_right(self, root):
        old_left = root.left
        new_left = old_left.right

        root.left = new_left
        old_left.right = root

        root.update_height()
        old_left.update_height()

        return old_left

    def _get_node(self, val):
    # assumes val is in tree
        curr = self.top_root
        while curr:
            if val <= curr.data:
                if val == curr.data and (curr.left is None or curr.left.data != val):
                    break
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def print(self):
        _print(self.top_root, 0, True)

def _print(root, depth, is_left_child):
    prefix = "<" if is_left_child else ">"
    if root is not None:
        print(" "*depth + prefix + str(root.val) + "," + str(root.height))
        _print(root.left, depth+1, True)
        _print(root.right, depth+1, False)

class AVLTreeNode:
    def __init__(self, val, height=0, left=None, right=None):
        self.val = val
        self.height = height
        self.left = left
        self.right = right

    def update_height(self):
        left_height = height(self.left)
        right_height = height(self.right)
        self.height = 1 + max(left_height, right_height)

    def balance_factor(self):
        return height(self.left) - height(self.right)

def min_descendant(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr

def max_descendant(node):
    curr = node
    while curr.right:
        curr = curr.right
    return curr

def height(node):
    if node is None:
        return -1
    else:
        return node.height

if __name__ == "__main__":
    main()
