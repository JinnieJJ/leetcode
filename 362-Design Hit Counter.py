from collections import deque

class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k = 300
        self.dq = deque()
        self.count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.getHits(timestamp)
        if self.dq and self.dq[-1][0] == timestamp:
            self.dq[-1][1] += 1
        else:
            self.dq.append([timestamp, 1])
        self.count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.dq and self.dq[0][0] <= timestamp - self.k:
            self.count -= self.dq.popleft()[1]
        return self.count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
