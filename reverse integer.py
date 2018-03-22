class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digit = []
        res = abs(x)
        while res>0:
            digit.append(res % 10)
            res = int(res/10)
        sum = 0
        for i in range(len(digit)):
            sum += digit[i]*(10**(len(digit)-i-1))
        if sum > 2147483647:
            return 0
        if x>0:
            return sum
        return -sum
