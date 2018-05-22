# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self.Recursion(0, len(preorder), 0, len(inorder))

    def Recursion(self, pre_start, pre_end, in_start, in_end):
        if pre_start == pre_end or in_start == in_end:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start:in_end + 1].index(root.val)
        root.left = self.Recursion(pre_start + 1, pre_start + offset + 1, in_start, in_start + offset)
        root.right = self.Recursion(pre_start + offset + 1, pre_end, in_start + offset + 1, in_end)
        return root
