# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        
        lRoot = self.upsideDownBinaryTree(root.left)
        rMost = lRoot
        while rMost.right:
            rMost = rMost.right
        root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)
        return root
