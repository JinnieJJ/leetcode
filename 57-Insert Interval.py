# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        
        for interval in intervals:
            current = result[-1]
            if interval.start <= current.end:
                current.end = max(interval.end, current.end) # pass by reference
            else:
                result.append(interval)
        return result
