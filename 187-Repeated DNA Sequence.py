class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ans = []
        valueCount = {}
        map = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
        sum = 0
        for x in range(len(s)):
            sum = (sum * 4 + map[s[x]]) & 0xFFFFF # sum*4 = sum << 2
            if x < 9:
                continue
            if sum not in valueCount:
                valueCount[sum] = 1
            else:
                valueCount[sum] += 1
            if valueCount[sum] == 2:
                ans.append(s[x - 9 : x + 1])
        return ans
