# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(-1)
        result.next = head
        tmp = result
        while tmp and tmp.next and tmp.next.next:
            node1 = tmp.next.next.next
            node2 = tmp.next.next
            node3 = tmp.next
            node2.next = None
            node3.next = None
            tmp.next = node2
            node2.next = node3
            node3.next = node1
            tmp = node3
        return result.next
