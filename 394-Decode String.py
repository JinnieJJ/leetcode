class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        digit = collections.defaultdict(int)
        alpha = collections.defaultdict(str)
        level = 1
        for c in s:
            if c.isdigit():
                digit[level] = digit[level] * 10 + int(c)
            elif c == '[':
                level += 1
            elif c == ']':
                alpha[level-1] += alpha[level] * digit[level-1]
                digit[level-1] = 0
                alpha[level] = ""
                level -= 1
            else:
                alpha[level] += c
        return alpha[1]
