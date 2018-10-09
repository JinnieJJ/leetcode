class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ans = 0
        cnt = collections.Counter(ages)
        for k1, v1 in cnt.items():
            for k2, v2 in cnt.items():
                if (k2 > 0.5*k1 + 7 and k2 <= k1):
                    # if both conditions met
                    ans += v1 * v2
                    if k1 == k2:
                        ans -= v1
        return ans
