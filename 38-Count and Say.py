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
        count = 1
        for i in range(len(seq)):
            if i < len(seq) - 1 and seq[i] == seq[i+1]:
                count += 1
            else:
                nextseq += str(count) + seq[i]
                count = 1
        return nextseq
