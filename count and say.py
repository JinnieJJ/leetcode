class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"
        for i in range(n-1):
            seq = self.Next(seq)
        return seq

    def Next(self, seq):
        nextseq = ""
        num = 1
        for i in range(len(seq)):
            if i < len(seq)-1 and seq[i] == seq[i+1]:
                num += 1
                continue
            nextseq += str(num)+seq[i]
            num = 1
        return nextseq
