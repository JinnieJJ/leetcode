# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        
        for interval in intervals:
            current = result[-1]
            if interval.start <= current.end:
                current.end = max(interval.end, current.end) # pass by reference
            else:
                result.append(interval)
        return result
