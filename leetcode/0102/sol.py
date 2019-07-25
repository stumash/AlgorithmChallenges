# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
    def enq(self, x):
        self.q.appendleft(x)
    def deq(self):
        return self.q.pop()
    def __bool__(self):
        return bool(self.q)

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        retval = []
        q = Queue()
        q.enq((root, 0))
        
        # bfs
        while q:
            treenode, depth = q.deq()
            if treenode:
                if len(retval) <= depth:
                    retval.append([])
                retval[depth].append(treenode.val)
                q.enq((treenode.left, depth+1))
                q.enq((treenode.right, depth+1))
        
        return retval
