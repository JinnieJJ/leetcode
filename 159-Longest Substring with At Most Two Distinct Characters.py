class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1 = p2 = currentp = None
        count1 = count2 = maxcount = currentcount = 0
        for c in s:
            if p1 is None or c == p1:
                p1 = c
                count1 += 1
            elif p2 is None or c == p2:
                p2 = c
                count2 += 1
            else:
                count = count1 + count2
                if count > maxcount:
                    maxcount = count
                
                p1, p2, currentp = currentp, c, c
                count1, count2, currentcount = currentcount, 1, 0
            
            if currentp == c:
                currentcount += 1
            else:
                currentp = c
                currentcount = 1
        return max(maxcount, count1+count2)
