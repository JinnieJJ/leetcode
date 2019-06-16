# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        dict = collections.defaultdict(list)
        
        def recursionHelper(parent, child):
            if parent and child:
                dict[parent.val].append(child.val)
                dict[child.val].append(parent.val)
            if child.left:
                recursionHelper(child, child.left)
            if child.right:
                recursionHelper(child, child.right)
        
        recursionHelper(None, root)
        
        res = [target.val]
        visited = set(res)
        for i in range(K):
            res = [y for x in res for y in dict[x] if y not in visited]
            visited = visited | set(res)
        return res
