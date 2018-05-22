# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.Recursion(root) >= 0

    def Recursion(self, root):
        if not root:
            return 0
        left, right = self.Recursion(root.left), self.Recursion(root.right)
        if left >= 0 and right >= 0 and abs(left - right) <= 1:
            return 1 + max(left, right)
        else:
            return -1
