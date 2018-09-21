class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        candies = [1]*size
        for i in range(size-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1
        for i in range(size-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        return sum(candies)
