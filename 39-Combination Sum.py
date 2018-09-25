class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.Recursion(sorted(candidates), results, 0, [], target)
        return results

    def Recursion(self, candidates, results, start, solution, target):
        if target == 0:
            results.append(list(solution))
        while start < len(candidates) and candidates[start] <= target:
            solution.append(candidates[start])
            self.Recursion(candidates, results, start, solution, target-candidates[start])
            solution.pop()
            start += 1
