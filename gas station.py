class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        min_sum, start, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if min_sum > total:
                min_sum, start = total, i + 1
        if total >= 0:
            return start
        return -1
