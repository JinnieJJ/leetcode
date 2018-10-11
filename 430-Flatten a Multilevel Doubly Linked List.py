"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr, stack = head, []
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future reattachment
                    stack.append(curr.next)
                curr.next, curr.child.prev, curr.child = curr.child, curr, None
            if not curr.next and len(stack):
                # If the current node is a child without a next pointer
                temp = stack.pop()
                temp.prev, curr.next = curr, temp
            curr = curr.next
        return head
