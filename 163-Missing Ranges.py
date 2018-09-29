class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        for num in nums:
            if lower > upper:
                return res
            if num == lower:
                lower += 1
            elif num == lower + 1:
                res.append(str(lower))
                lower = num + 1
            elif num > lower + 1:
                res.append(str(lower)+"->"+str(num-1))
                lower = num + 1
        if lower == upper:
            res.append(str(upper))
        if lower < upper:
            res.append(str(lower)+"->"+str(upper))
        return res
