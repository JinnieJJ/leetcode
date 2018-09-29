class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        input = input.split('\n')
        maxlen = 0
        dict = {-1:0}
        for f in input:
            name = f.lstrip('\t')
            depth = len(f) - len(name)
            if '.' in name:
                maxlen = max(maxlen, dict[depth-1] + len(name))
            else:
                dict[depth] = dict[depth-1] + len(name) + 1
        return maxlen
