class Solution:
    def generateParentheses(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.ParenthesesRecursion(results, n, n, "")
        return results

    def ParenthesesRecursion(self, results, left, right, parentheses):
        if left == 0 and right == 0:
            results.append(parentheses)
        if left > 0:
            self.ParenthesesRecursion(results, left-1, right, parentheses+"(")
        if left < right:
            self.ParenthesesRecursion(results, left, right-1, parentheses+")")
