class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        secretcount = [0] * 10
        guesscount = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                secretcount[int(secret[i])] += 1
                guesscount[int(guess[i])] += 1
        for i in range(10):
            B += min(secretcount[i], guesscount[i])

        return str(A) + 'A' + str(B) + 'B'
