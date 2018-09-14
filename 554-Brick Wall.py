class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        maxCount = 0
        crackCounter = {}
        for row in wall:
            crack = 0
            for i in range(len(row) - 1): #空隙的数量
                crack += row[i]
                if crack not in crackCounter:
                    crackCounter[crack] = 1
                else:
                    crackCounter[crack] += 1
                maxCount = max(maxCount, crackCounter[crack])
                
        return len(wall) - maxCount
