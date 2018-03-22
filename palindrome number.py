class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        res = x
        digit = 0
        pal = 0
        
        while res>0:
            digit = res%10
            res = int(res/10)
            pal = pal*10+digit
        
        return x==pal
