class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        n = len(num)
        for i in range((n+1)//2):
            if num[n-1-i] not in lookup or num[i] != lookup[num[n-1-i]]:
                return False
        return True
