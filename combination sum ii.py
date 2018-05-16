class Solution:
    def combinationSum2(self, candidates, target):
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
            # print results
        previous = 0
        while start < len(candidates) and candidates[start] <= target:
            if previous != candidates[start]:
                solution.append(candidates[start])
                self.Recursion(candidates, results, start+1, solution, target-candidates[start])
                # print str(start)+":"
                # print solution
                solution.pop()
                previous = candidates[start]
            start += 1
