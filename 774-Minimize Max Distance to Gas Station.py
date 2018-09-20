class Solution:
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """  
       # 用priority queue会时间超标, 二分法不会
        stations.sort()
        left, right = 0, 1e9
        step = 1e-9
        while left <= right:
            mid = (left + right) / 2
            if self.isValid(stations, K, mid):
                right = mid - step
            else:
                left = mid + step
        return mid
            
    def isValid(self, stations, K, gap):
        for x in range(len(stations) - 1):
            dist = stations[x+1] - stations[x]
            K -= int(math.ceil(dist / gap)) - 1
        return K>=0
