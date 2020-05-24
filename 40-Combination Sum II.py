class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates = sorted(candidates)
        res = set()
        
        def helper(end, selected, target):
            if target < 0:
                return
            if target == 0:
                res.add(tuple(selected))
            for i in range(end, -1, -1):
                if candidates[i] > target:
                    continue
                elif i < end and candidates[i] == candidates[i+1]: # avoid duplicates
                    continue
                helper(i - 1, selected + [candidates[i]], target - candidates[i])
         
        helper(len(candidates) - 1, [], target)
        res = [list(x) for x in res]
        return res
