class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        
        if not str:
            return 0
        
        index = 0
        while index<len(str) and str[index].isspace():
            index += 1
        sign = 1
        if str[index] == "+":
            index += 1
        elif str[index] == "-":
            sign = -1
            index += 1
        
        res = 0
        while index < len(str) and '0' <= str[index] <= '9':
            res = res*10+int(str[index])
            index += 1
            if res>INT_MAX:
                return INT_MAX if sign==1 else INT_MIN
        
        return res*sign
