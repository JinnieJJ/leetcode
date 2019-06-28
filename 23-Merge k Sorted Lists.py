import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(-1)
        cur = result
        
        h = []
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, node))
        
        while len(h) > 0:
            cur.next = heapq.heappop(h)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(h, (cur.next.val, cur.next))
        return result.next
