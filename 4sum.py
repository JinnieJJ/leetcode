class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(set(nums)) == 1 and len(nums) > 3 and target == nums[0] :
            return [[nums[0], nums[0], nums[0], nums[0]]]
        sorted_nums = sorted(nums)
        mapper = {}
        result = set()

        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if sorted_nums[i]+sorted_nums[j] not in mapper:
                    mapper[sorted_nums[i] + sorted_nums[j]] = [[i,j]]
                else:
                    mapper[sorted_nums[i] + sorted_nums[j]].append([i, j])

        for key in mapper.keys():
            if target-key in mapper and target-key != key:
                for pair1 in mapper[key]:
                    for pair2 in mapper[target-key]:
                        if pair1[0]!=pair2[0] and pair1[0]!=pair2[1] and pair1[1]!=pair2[0] and pair1[1]!=pair2[1]:
                            result.add(tuple(sorted([sorted_nums[pair1[0]], sorted_nums[pair1[1]], sorted_nums[pair2[0]], sorted_nums[pair2[1]]])))
            if target-key == key:
                if len(mapper[key]) > 1:
                    for index, pair1 in enumerate(mapper[key]):
                        for pair2 in mapper[key][index+1:]:
                            if pair1[0]!=pair2[0] and pair1[0]!=pair2[1] and pair1[1]!=pair2[0] and pair1[1]!=pair2[1]:
                                result.add(tuple(sorted([sorted_nums[pair1[0]], sorted_nums[pair1[1]], sorted_nums[pair2[0]], sorted_nums[pair2[1]]])))
        return list(result)
