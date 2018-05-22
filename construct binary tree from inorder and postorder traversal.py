# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.postorder = postorder
        self.inorder = inorder
        return self.Recursion(0, len(inorder))

    def Recursion(self, start, end):
        if start < end:
            root = TreeNode(self.postorder.pop())
            index = self.inorder.index(root.val)
            root.right = self.Recursion(index + 1, end)
            root.left = self.Recursion(start, index)
            return root
        return None
