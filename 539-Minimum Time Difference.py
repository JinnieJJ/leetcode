class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def helper(time):
            hour, minute = map(int, time.split(":"))
            return hour * 60 + minute
        
        times = sorted(helper(time) for time in timePoints)
        ans = 24 * 60
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i-1])
        return min(24 * 60 + times[0] - times[-1], ans)
