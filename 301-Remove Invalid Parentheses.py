class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        result = []
        q = [s]
        visited = set([s])
        found = False
        while q:
            curr = q.pop(0)
            if self.isValid(curr):
                found = True
                result.append(curr)
            elif not found:
                for i in range(len(curr)):
                    if curr[i] == '(' or curr[i] == ')':
                        tmp = curr[:i] + curr[i + 1:]
                        if tmp not in visited:
                            q.append(tmp)
                            visited.add(tmp)
        return result


    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
