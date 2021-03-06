class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        if not digits:
            return []
        
        result = [""]
        for digit in reversed(digits): # 3 2
            letters = mapper[int(digit)] #[d,e,f] [a b c]
            m = len(letters) #3 3
            n = len(result) #1 3
            result += [result[i%n] for i in range(n, m*n)] # ["", "", ""] [d, e, f, d, e, f, d, e, f]

            for i in range(m*n):
                result[i] = letters[int(i/n)] + result[i] # [d, e, f] [ad, ae, af, bd, be, bf, cd, ce, cf]
            
        return result
    
class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if not digits:
            return []

        result = []
        self.dfs(digits, mapper, result, 0, "")
        return result

    def dfs(self, digits, mapper, result, start, solution):
        if start == len(digits):
            result.append(solution)
        else:
            for c in mapper[int(digits[start])]:
                solution += c
                self.dfs(digits, mapper, result, start+1, solution)
                solution = solution[:-1]

    
