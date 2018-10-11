class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(word)  and j < len(abbr):
            if abbr[j] == word[i]:
                i += 1
                j += 1
            elif '0' <= abbr[j] <= '9':
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and '0' <= abbr[j] <= '9':
                    num = 10 * num + (ord(abbr[j]) - ord('0'))
                    j += 1
                i += num
            else:
                break
        return i == len(word) and j == len(abbr)
