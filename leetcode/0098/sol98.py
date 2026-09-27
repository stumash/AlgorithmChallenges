class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if not self.isValidNodeInBst(root.left, None, root.val):
                return False
        if root.right is not None:
            if not self.isValidNodeInBst(root.right, root.val, None):
                return False
        return True

    def isValidNodeInBst(self, node: TreeNode, minVal: int | None, maxVal: int | None) -> bool:
        if maxVal is not None and not (node.val < maxVal):
            return False
        if minVal is not None and not (node.val > minVal):
            return False
        if node.left:
            newMaxVal = min(maxVal, node.val) if maxVal is not None else node.val
            if not self.isValidNodeInBst(node.left, minVal, newMaxVal):
                return False
        if node.right:
            newMinVal = max(minVal, node.val) if minVal is not None else node.val
            if not self.isValidNodeInBst(node.right, newMinVal, maxVal):
                return False
        return True


ex1 = (
    TreeNode(0,
        None,
        TreeNode(-1),
    )
)

s = Solution()
print(s.isValidBST(None))
print(s.isValidBST(ex1))

