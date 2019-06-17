# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict = collections.defaultdict(list)
        self.depth(root, dict)
        res = []
        for k in sorted(dict.keys()):
            res.append(dict[k])
        return res
    
    def depth(self, root, dict):
        if not root:
            return 0
        left = self.depth(root.left ,dict)
        right = self.depth(root.right, dict)
        depth = max(left, right) + 1
        dict[depth].append(root.val)
        # print(dict)
        return depth
