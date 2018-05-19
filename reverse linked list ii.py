class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        for _ in range(m - 1):
            node = node.next
        prev = node.next
        curr = prev.next
        for _ in range(n - m):
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        node.next.next = curr
        node.next = prev
        return dummy.next
