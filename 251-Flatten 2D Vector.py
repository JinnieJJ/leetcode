class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.stack = vec2d
        self.i = 0
        self.j = -1

    def next(self):
        """
        :rtype: int
        """
        return self.stack[self.i][self.j]

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        self.j += 1
        while True:
            if self.j < len(self.stack[self.i]):
                return True
            self.i += 1
            if self.i >= len(self.stack):
                return False
            self.j = 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
