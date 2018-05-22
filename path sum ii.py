# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.Recursion(root, sum, [], result)
        return result

    def Recursion(self, root, sum, curr, result):
        if not root:
            return
        sum -= root.val
        if sum == 0 and root.left is None and root.right is None:
            result.append(curr + [root.val])
        if root.left:
            self.Recursion(root.left, sum, curr + [root.val], result)
        if root.right:
            self.Recursion(root.right, sum, curr + [root.val], result)
