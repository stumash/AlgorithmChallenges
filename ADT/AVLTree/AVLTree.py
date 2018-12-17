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

    for num in random_half(nums):
        print("deleting {}".format(num))
        tree.remove(num)
    print()
    tree.print()

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

    def remove(self, val):
        node = self._get_node(val)
        self.top_root = self._remove(self.top_root, node)

    def _remove(self, root, node):
        if not root:
            return root
        elif node.val < root.val:
            root.left = self._remove(root.left, node)
        elif node.val > root.val:
            root.right = self._remove(root.right, node)

        elif node is root:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            succ = min_descendant(root.right)
            root.val = succ.val
            root.right = self._remove(root.right, succ)

        if root is None:
            return root

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
        curr = self.top_root
        while curr:
            if curr is None:
                raise ValueError('not found')
            if val <= curr.val:
                if val == curr.val and (curr.left is None or curr.left.val != val):
                    break
                curr = curr.left
            else:
                curr = curr.right
        if not curr: raise ValueError('not found')
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
