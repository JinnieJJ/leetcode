class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n <= 0 or n > 45:
            return []
        res = set()
        
        def helper(end, selected, target):
            if target == 0 and len(selected) == k:
                res.add(tuple(selected))
                return
            elif target <= 0 or len(selected) >= k:
                return
            for i in range(end, 0, -1):
                if i > target:
                    continue
                helper(i - 1, selected + [i], target - i)
        
        helper(9, [], n)
        res = [list(x) for x in res]
        return res
