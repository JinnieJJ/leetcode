class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        lastchar = '+'
        s += '+'
        for char in s:
            if ord('0') <= ord(char) <= ord('9'):  # digit
                num = num * 10 + ord(char) - ord('0')
            
            else:
                if char != ' ':
                    if lastchar == '+':  # last sign
                        stack.append(num)
                    elif lastchar == '-':
                        stack.append(-num)
                    elif lastchar == '*':
                        last = stack.pop()
                        stack.append(last*num)
                    elif lastchar == '/':
                        last = stack.pop()
                        if last < 0:
                            res = -(-last//num)
                        else:
                            res = last//num
                        stack.append(res)
                    
                    lastchar = char
                    num = 0
        return sum(stack)
