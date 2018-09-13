class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = list(map(int, str(num)))
        a_sorted = sorted(a, reverse=True)
        
        for i in range(len(a)):
            if a_sorted[i] > a[i]:
                idx = len(a) - 1 - a[::-1].index(a_sorted[i])
                a[i], a[idx] = a[idx], a[i]
                break
        return int(''.join(map(str, a)))
