# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.result = 0
        if self.dfs(root) == "not":
            self.result += 1
        return self.result
        
        
    def dfs(self, root):
        if not root:
            return "covered"
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == "not" or right == "not":
            self.result += 1
            return "camera"
        if left == "camera" or right == "camera":
            return "covered"
        return "not"
