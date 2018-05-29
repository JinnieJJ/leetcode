class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    if first * second < 0:
                        stack.append(-(abs(first) // abs(second)))
                    else:
                        stack.append(first // second)
        return stack.pop()
        
