class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        counts = collections.Counter(word.strip("!?',;.") for word in paragraph.lower().split())
        lookup = set(banned)

        result = ''
        for word in counts:
            if (not result or counts[word] > counts[result]) and word not in lookup:
                result = word
        return result
            
