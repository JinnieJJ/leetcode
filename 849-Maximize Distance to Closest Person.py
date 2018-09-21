class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev_seat = -1
        max_gap = 1
        for i in range(len(seats)):
            if seats[i]:
                if prev_seat < 0:
                    max_gap = i
                else:
                    max_gap = max(max_gap, (i - prev_seat) // 2)
                prev_seat = i
        return max(max_gap, len(seats) - 1 - prev_seat)
