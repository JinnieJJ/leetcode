class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = time[:2] + time[3:]
        isValid = lambda t:int(t[:2]) < 24 and int(t[2:]) < 60
        
        sorted_time = sorted(time)
        for i in range(3, -1, -1):
            for s in sorted_time:
                if s <= time[i]:
                    continue
                next_time = time[:i]+s+sorted_time[0]*(3-i)
                if  isValid(next_time):
                    return next_time[:2]+":"+next_time[2:]
        
        return sorted_time[0]*2+":"+sorted_time[0]*2
