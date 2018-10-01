class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.printed = set()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.q and self.q[0][1] <= timestamp - 10:
            self.printed.remove(self.q.popleft()[0])
        if message in self.printed:
            return False
        self.q.append((message, timestamp))
        self.printed.add(message)
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
