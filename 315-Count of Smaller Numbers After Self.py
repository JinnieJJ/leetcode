class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)

    def lowbit(self, x):
        return x & -x

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = {}
        for k, v in enumerate(sorted(set(nums))):
            index[v] = k+1
        iNums = [index[i] for i in nums]  # 排序+去重
        print(iNums)
        ft = FenwickTree(len(iNums))
        ans = [0] * len(nums)
        for i in range(len(iNums)-1, -1, -1):  # 从后往前依次加入树中
            ans[i] = ft.sum(iNums[i] - 1)  # 找已经在书中的（说明在nums中的位置在i后面），sum(iNums[i] - 1)找所有比nums[i]小的
            ft.add(iNums[i], 1)
            print(ft.sums)
        return ans

print(Solution().countSmaller([1, 4, 5, 9, 8, 1, 2]))
