class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ""
        step = 2*numRows-2
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if 0<i<numRows-1 and j+2*(numRows-1-i) < len(s):
                    zigzag += s[j+2*(numRows-1-i)]
        return zigzag
