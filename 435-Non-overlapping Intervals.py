# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0: 
            return 0
        intervals.sort(key = lambda x: x.start)
			
        count = 0
        prev_interval = intervals[0]
        for cur_interval in intervals[1:]:
            # Case 1: Don't overlap
            if cur_interval.start >= prev_interval.end:
                prev_interval = cur_interval
            # Case 2: Overlap
            else:
                count += 1
                if prev_interval.end > cur_interval.end: 
                    prev_interval = cur_interval
        return count
