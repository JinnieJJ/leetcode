# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        leftheight = 0
        tmp = root
        while tmp.left:
            leftheight += 1
            tmp = tmp.left
        
        rightheight = 0
        tmp = root
        while tmp.right:
            rightheight += 1
            tmp = tmp.right
        
        if leftheight == rightheight:
            return (1 << (leftheight+1)) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    
        
    
    # 算height
    # 如果右边的height = h-1 那么就是2**h+右边的recursion
    # 如果右边的height = h-2 那么就是左边的recursion+2**(h-1)
