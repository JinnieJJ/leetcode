# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        self.cache = {}
        return self.Recursion(1, n)

    def Recursion(self, start, end):
        if (start, end) not in self.cache:
            roots = []
            for root in range(start, end + 1):
                for left in self.Recursion(start, root - 1):
                    for right in self.Recursion(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        roots.append(node)
            self.cache[(start, end)] = roots
        return self.cache[(start, end)] or [None]
