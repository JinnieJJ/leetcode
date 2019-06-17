# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [(root, 0, 0)]
        curDepth = 0
        left = 0
        ans = 0
        
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2+1))
                if curDepth != depth:
                    curDepth = depth
                    left = pos
                ans = max(ans, pos - left + 1)
        return ans
