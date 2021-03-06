# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        curr_level = [root]
        reverse = False
        while curr_level:
            level_result = []
            next_level = []
            for node in curr_level:
                level_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if reverse:
                level_result.reverse()
                reverse = False
            else:
                reverse = True
            result.append(level_result)
            curr_level = next_level
        return result
