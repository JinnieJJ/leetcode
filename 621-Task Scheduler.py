class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        output = [0] * 26
        for task in tasks:
            output[ord(task)-ord('A')] += 1
        
        maxOutput = max(output)
        count = 0
        for i in output:
            if i == maxOutput:
                count += 1
        
        return max(len(tasks), (maxOutput - 1) * (n + 1) + count)
