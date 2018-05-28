# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while root or stack:
            if not root:
                root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
        return result
