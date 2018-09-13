# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        inorder = []
        self.inorderTraversal(root, inorder)
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True
    
    def inorderTraversal(self, root, inorder):
        if root:
            self.inorderTraversal(root.left, inorder)
            inorder.append(root.val)
            self.inorderTraversal(root.right, inorder)

 # Inorder Traversal in increasing order
