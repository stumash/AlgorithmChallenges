#!/usr/bin/env python3.6

from typing import Optional, Deque
from collections import deque

from random import sample
shuffled = lambda l: sample(l, len(l))

def main():
    tree = AvlTree()
    for i in range(50):
        tree.insert(i)
    tree.print()
    print("avl tree {} valid".format("is" if validate_avl_tree(tree) else "isn't"))

class AvlTreeNode:
    def __init__(self, parent, data, height):
        self.parent = parent
        self.data = data
        self.height = height
        self.left = None
        self.right = None

    def update_height(self) -> None:
        self.height = 1 + max(get_height(self.left), get_height(self.right))

def get_height(tn: AvlTreeNode) -> int:
    return -1 if tn is None else tn.height

class AvlTree:
    def __init__(self):
        self.root: Optional[AvlTreeNode] = None

    def insert(self, data):
        if self.root is None:
            self.root = AvlTreeNode(None, data, 0)
            return
        path = self._bst_insert(data)
        for tn in reversed(path):
            self._rebalance(tn)

    def _bst_insert(self, data) -> Deque[AvlTreeNode]:
        path: Deque[AvlTreeNode] = self._bst_parent_path(data)
        if data <= path[-1].data:
            path[-1].left = AvlTreeNode(path[-1], data, 0)
        else:
            path[-1].right = AvlTreeNode(path[-1], data, 0)
        return path

    def _bst_parent_path(self, data) -> Deque[AvlTreeNode]:
        path: Deque[AvlTreeNode] = deque()
        curr = self.root
        while True:
            if curr is None:
                break
            path.append(curr)
            if data <= curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return path

    def remove(self, data) -> None:
        path: Deque[AvlTreeNode] = self._bst_parent_path(data)
        parent = path[-1]

        if parent.left is not None and parent.left.data == data:
            curr = parent.left
        elif parent.right is not None and parent.right.data == data:
            curr = parent.right
        else:
            raise ValueError('Value not found')

        if curr.left is None and curr.right is None:
            if parent.left is curr:
                parent.left is None
            else:
                parent.right is None
        elif curr.left is None:
            if parent.left is curr:
                parent.left = curr.right
            else:
                parent.right = curr.right
        elif curr.right is None:
            if parent.left is curr:
                parent.left = curr.left
            else:
                parent.right = curr.left
        else: # both not None
            # TODO replace with successor
            replacement = self.succ(curr)
            raise ValueError('not implemented')

        for node in reversed(path):
            self._rebalance(node)

        return curr

    def succ(self, tn: AvlTreeNode) -> AvlTreeNode:
        if tn.right is not None:
            return self._min_descendant(tn.right)
        else:
            raise ValueError('not implemented')

    def pred(self, tn: AvlTreeNode) -> AvlTreeNode:
        raise ValueError('not implemented')

    def _get_node(self, data) -> AvlTreeNode:
        path = self._bst_parent_path(data)
        parent = path[-1]
        if parent.left is not None and parent.left.data == data:
            return parent.left
        elif parent.right is not None and parent.right.data == data:
            return parent.right
        else:
            raise ValueError('Value not found')

    def __contains__(self, data) -> bool:
        path = self._bst_parent_path(data)
        parent = path[-1]
        if parent.left is not None and parent.left.data == data:
            return True
        elif parent.right is not None and parent.right.data == data:
            return True
        else:
            return False

    def _rebalance(self, tn: AvlTreeNode) -> None:
        tn.update_height()
        balance_factor = get_height(tn.left) - get_height(tn.right)
        if balance_factor > 1:
            balance_factor_2 = get_height(tn.left.left) - get_height(tn.left.right)
            if balance_factor_2 > 1: # left-left case
                self._rotate_clockwise(tn)
            else:                    # left-right case
                self._rotate_counterclockwise(tn.left)
                self._rotate_clockwise(tn)
        elif balance_factor < -1:
            balance_factor_2 = get_height(tn.right.left) - get_height(tn.right.right)
            if balance_factor_2 > 1: # right-left case
                self._rotate_clockwise(tn.right)
                self._rotate_counterclockwise(tn)
            else:                    # right-right case
                self._rotate_counterclockwise(tn)

    def _rotate_clockwise(self, tn: AvlTreeNode) -> None:
        old_parent = tn.parent
        old_left = tn.left

        if old_parent is not None:
            if tn is old_parent.left:
                old_parent.left = old_left
            else:
                old_parent.right = old_left

        tn.left = old_left.right
        tn.parent = old_left
        tn.parent.right = tn
        tn.parent.parent = old_parent

        tn.update_height()
        tn.parent.update_height()

        if old_parent is not None:
            old_parent.update_height()
        else:
            self.root = tn.parent

    def _rotate_counterclockwise(self, tn: AvlTreeNode) -> None:
        old_parent = tn.parent
        old_right = tn.right

        if old_parent is not None:
            if tn is old_parent.left:
                old_parent.left = old_right
            else:
                old_parent.right = old_right

        tn.right = old_right.left
        tn.parent = old_right
        tn.parent.left = tn
        tn.parent.parent = old_parent

        tn.update_height()
        tn.parent.update_height()

        if old_parent is not None:
            old_parent.update_height()
        else:
            self.root = tn.parent

    def _min_descendant(self, tn: AvlTreeNode) -> AvlTreeNode:
        curr = tn
        while curr.left is not None:
            curr = curr.left
        return curr

    def _max_descendant(self, tn: AvlTreeNode) -> AvlTreeNode:
        curr = tn
        while curr.right is not None:
            curr = curr.right
        return curr

    def print(self):
        _print(self.root, 0)

def _print(tn: AvlTreeNode, depth: int):
    if tn is not None:
        print(" "*depth+str(tn.data)+","+str(tn.height))
        _print(tn.left, depth+1)
        _print(tn.right, depth+1)

def validate_avl_tree(t: AvlTree):
    inorder = deque()

    _validate_avl_tree(t.root, inorder)

    return all(inorder[i] < inorder[i+1] for i in range(len(inorder)-1))

def _validate_avl_tree(tn: AvlTreeNode, inorder):
    if tn is None: return
    _validate_avl_tree(tn.left, inorder)
    inorder.append(tn.data)
    _validate_avl_tree(tn.right, inorder)

if __name__ == "__main__":
    main()
