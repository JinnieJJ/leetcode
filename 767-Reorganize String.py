class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        char2cnt = collections.Counter(S)
        char_cnt = char2cnt.most_common(len(char2cnt))
        
        topchar, topcnt = char_cnt.pop(0)
        if 2 * topcnt - len(S) > 1: 
            return ""
        
        seqs = list(topchar for i in range(topcnt))
        i = 0
        for char, cnt in char_cnt:
            while cnt > 0:
                seqs[i] += char
                i = (i + 1) % topcnt
                cnt -= 1
        return "".join(seqs)
