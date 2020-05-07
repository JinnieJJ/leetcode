# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if node.val <= lower or node.val >= upper:
                return False
            if node.left:
                stack.append((node.left, lower, node.val))
            if node.right:
                stack.append((node.right, node.val, upper))
        return True
