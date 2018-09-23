from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        # all numbers in maxHeap should be no greater than numbers in minHeap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.maxHeap, -num)
        if self.minHeap and self.maxHeap:
            minTop = self.minHeap[0]
            maxTop = self.maxHeap[0]
            if -maxTop > minTop:
                heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) - 1 > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


    def findMedian(self):
        """
        :rtype: float
        """
        if not self.maxHeap:
            return None
        if len(self.minHeap) < len(self.maxHeap):
            return -float(self.maxHeap[0])
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
