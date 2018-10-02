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
        def helper(root, cur_height, max_height):
            # in this case, now we are already in the bottom level
            # return 1 if this is a leaf
            if cur_height == max_height:
                if root is None:
                    return 0
                else:
                    return 1
										
            # right most child in the bottom level of the left child happens to be the middle point
            tmp = root.left
            tmp_height = cur_height + 1
            while tmp_height < max_height:
                tmp = tmp.right
                tmp_height += 1
            if tmp is None:
                # if middle point is not leaf, looking at the left part, which means recursively process the left child
                return helper(root.left, cur_height + 1, max_height)
            else:
                # if middle point is a leaf, looking at the left part, which means recursively process the left child
                # and every thing in the left part are leaves, so don't forget this part
                return pow(2, max_height - cur_height - 1) + helper(root.right, cur_height + 1, max_height)
        
        
        if root is None:
            return 0
        height = 0
        tmp = root
        # Go to the left most child in bottom level, to count the height of this tree
        while tmp.left is not None:
            tmp = tmp.left
            height += 1
        # second term represents are the node above the bottom level
        return helper(root, 0, height) + pow(2, height) - 1
