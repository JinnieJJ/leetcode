# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        visited = {}
        node = head
        while node:
            visited[node] = RandomListNode(node.label)
            node = node.next
        
        node = head
        while node:
            visited[node].next = visited[node.next] if node.next else None
            visited[node].random = visited[node.random] if node.random else None
            node = node.next
        return visited[head]
    
    """
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        node = head
        while node:
            copyNode = Node(node.val, node.next, None)
            node.next = copyNode
            node = copyNode.next
        
        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next
        
        oldPtr = head
        newPtr = head.next
        copyHead = head.next
        while oldPtr:
            oldPtr.next = oldPtr.next.next
            newPtr.next = newPtr.next.next if newPtr.next else None
            oldPtr = oldPtr.next
            newPtr = newPtr.next
        
        return copyHead
