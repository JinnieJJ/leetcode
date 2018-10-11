class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        if len(num2) > len(num1):
            return self.addStrings(num2, num1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        num2 += '0' * (len(num1) - len(num2))

        carrier = 0
        ans = ''
        for i in range(len(num1)):
            ans += str((int(num1[i]) + int(num2[i]) + carrier) % 10)
            carrier = (int(num1[i]) + int(num2[i]) + carrier) // 10
        if carrier != 0:
            ans += str(carrier)
        return ans[::-1]
