class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'  # default
        s += '+'  # add a char to force it processing the last number
        for char in s:
            if ord('0') <= ord(char) <= ord('9'):  # digit
                num = num * 10 + ord(char) - ord('0')
            else:  # finish scanning a number
                if char != ' ':
                    if sign == '+':  # last sign
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        last = stack.pop()
                        stack.append(last*num)
                    elif sign == '/':
                        last = stack.pop()
                        if last < 0:
                            res = -(-last//num)
                        else:
                            res = last//num
                        stack.append(res)

                    # reset
                    sign = char
                    num = 0

        return sum(stack)
