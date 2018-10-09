# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf4 = [''] * 4
        self.i4 = 0
        self.n4 = 0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.i4 < self.n4:
                buf[i] = self.buf4[self.i4]
                i += 1
                self.i4 += 1
            else:
                self.n4 = read4(self.buf4)
                if self.n4:
                    self.i4 = 0
                else:
                    break
        return i

    
