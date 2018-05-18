# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            after = cur.next
            while after and after.val == cur.val:
                after = after.next
            cur.next = after
            cur = cur.next
        return head
