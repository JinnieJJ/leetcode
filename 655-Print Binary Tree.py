# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def getHeight(node):
            return 0 if not node else 1 + max(getHeight(node.left), getHeight(node.right))
        
        def updateOutput(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid]  = str(node.val)
            updateOutput(node.left, row+1, left, mid-1)
            updateOutput(node.right, row+1, mid+1, right)
        
        height = getHeight(root)
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        updateOutput(root, 0, 0, width-1)
        return self.output
        
        
            
