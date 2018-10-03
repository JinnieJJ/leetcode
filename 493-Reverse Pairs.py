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
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = [n*2 for n in nums]
        dict = {v: k+1 for k, v in enumerate(sorted(set(nums+nums2)))}
        print(dict)
        ft = FenwickTree(len(dict))
        ans = 0
        for n in nums2[::-1]:
            ans += ft.sum(dict[n/2]-1)
            ft.add(dict[n], 1)
            print(ft.sums)
        return ans


print(Solution().reversePairs([1, 4, 2]))
