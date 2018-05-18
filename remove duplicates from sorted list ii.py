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
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val;
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = None
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next
