class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        value = 0
        carry = 0
        if len(a) < len(b):
            return self.addBinary(b, a)
        for i in range(len(a)):
            val = carry
            val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = int(val/2), val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]
