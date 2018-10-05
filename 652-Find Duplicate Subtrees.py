# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        treeMap = collections.defaultdict(list)
        def flattenTree(root):
            if not root:
                ans = '#'
            else:
                ans = '%s(%s,%s)' % (root.val, flattenTree(root.left), flattenTree(root.right))
                treeMap[ans].append(root)
            return ans
        flattenTree(root)
        return [v[0] for v in treeMap.values() if len(v) > 1]
