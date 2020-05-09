class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        step = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), step):
                res += s[j]
                if 0 < i < numRows - 1 and j + 2 * (numRows - 1- i) < len(s):
                    res += s[j + 2 * (numRows - 1- i)]
        return res
