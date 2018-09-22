class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        for i in range(1, target+1):
            # 2^(k-1) <= i < 2^k
            k  = i.bit_length()
            if i == 2**k - 1:
                # case 1. drive exactly i at best
                dp[i] = k            
            else:
                # case 2. drive cross i at 2^k-1, and turn back to i
                #         seq(i) = A^k -> R -> seq(2^k-1 - i)
                dp[i] = k + 1 + dp[(2**k-1) - i]
                for j in range(k-1):
                    # case 3. drive less then 2^k-1, and turn back some distance,
                    #         and turn back again to make the direction is the same
                    #         seq(i) = shortest(seq(i), A^(k-1) -> R -> A^j -> R -> seq(i - (2^(k-1)-1) + (2^j-1)))
                    dp[i] = min(dp[i], (k-1) + 1 + j + 1 + dp[i - ((2**(k-1)-1) - (2**j-1))])
        return dp[target]
