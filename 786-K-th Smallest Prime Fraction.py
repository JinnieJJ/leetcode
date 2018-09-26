class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        pq = [(A[0]/A[i], 0, i) for i in range(len(A)-1, 0, -1)]
        for _ in range(K-1):
            frac, i, j = heapq.heappop(pq)
            i += 1
            if i < j:
                heapq.heappush(pq, (A[i]/A[j], i, j))

        return A[pq[0][1]], A[pq[0][2]]
        
class Solution:
    def kthSmallestPrimeFraction(self, primes, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        from fractions import Fraction
        def under(x):
            count = best = 0
            i = 0
            for j in range(1, len(primes)):
                while primes[i] < primes[j] * x:
                    i += 1
                count += i
                if i > 0:
                    best = max(best, Fraction(primes[i-1], primes[j]))
            return count, best

        lo, hi = 0.0, 1.0
        while lo + 1e-9 < hi:
            mi = (lo + hi) / 2.0
            count, best = under(mi)
            if count < K:
                lo = mi
            else:
                ans = best
                hi = mi
        return ans.numerator, ans.denominator        
