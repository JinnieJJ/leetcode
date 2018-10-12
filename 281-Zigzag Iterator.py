from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = deque([])
        self.lists = [v1,v2]
        if v1: 
            self.q.append((0,0))
        if v2: 
            self.q.append((1,0))
        

    def next(self):
        """
        :rtype: int
        """
        i, pos = self.q.popleft()
        num = self.lists[i][pos]
        pos += 1
        if pos < len(self.lists[i]):
            self.q.append((i, pos))
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.q
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
