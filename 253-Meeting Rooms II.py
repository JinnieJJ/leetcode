# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start = sorted(start)
        end = sorted(end)
            
        count = 0
        current_count = 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                current_count += 1
                count = max(count, current_count)
                s += 1
            else:
                current_count -= 1
                e += 1
        return count
