# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = None
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        return dummy.next
