class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(set(nums)) == 1 and len(nums) > 3 and target == nums[0]:
            return [[nums[0], nums[0], nums[0], nums[0]]]
        nums = sorted(nums)
        mapper = collections.defaultdict(list)
        res = set()

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                mapper[nums[i] + nums[j]].append([i, j])

        for key in mapper.keys():
            if target - key in mapper and target - key != key:
                for p1 in mapper[key]:
                    for p2 in mapper[target - key]:
                        if p1[0] != p2[0] and p1[0] != p2[1] and p1[1] != p2[0] and p1[1] != p2[1]:
                            res.add(tuple(sorted((nums[p1[0]], nums[p1[1]], nums[p2[0]], nums[p2[1]]))))

            if target - key == key:
                if len(mapper[key]) > 1:
                    for i, p1 in enumerate(mapper[key]):
                        for p2 in mapper[key][i+1:]:
                            if p1[0] != p2[0] and p1[0] != p2[1] and p1[1] != p2[0] and p1[1] != p2[1]:
                                res.add(tuple(sorted((nums[p1[0]], nums[p1[1]], nums[p2[0]], nums[p2[1]]))))
        return list(res)
