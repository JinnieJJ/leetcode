class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        curNum = 0
        i = 0
        stack = []
        
        def calculate(oper, num):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-1 * num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            
        while i < len(s):
            if s[i].isdigit():
                curNum = curNum * 10 + int(s[i])
            elif s[i] == '(':
                stack.append(sign)
                stack.append(s[i])
                curNum, sign = 0, "+"

            if s[i] in "+-*/)":
                calculate(sign, curNum)
                sign = s[i] if s[i] in '+-*/' else sign
                curNum = 0 
                
                if s[i] == ')':
                    curNum = 0
                    while stack[-1] != '(':
                        curNum += stack.pop()
                    stack.pop()  # '('
                    sign = stack.pop()
            i += 1
            
        calculate(sign, curNum)
        return sum(stack)
