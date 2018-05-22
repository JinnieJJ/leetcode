# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        node, length = head, 0
        while node:
            node = node.next
            length += 1
        self.curr = head
        return self.Recursion(0, length - 1)

    def Recursion(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        left = self.Recursion(left, mid - 1)
        root = TreeNode(self.curr.val)
        root.left = left
        self.curr = self.curr.next
        root.right = self.Recursion(mid + 1, right)
        return root
