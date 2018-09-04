class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        # Init bucket
        a, b = min(nums), max(nums)
        bucket_range = max(1, (b - a) // (n - 1))
        bucket_count = (b - a) // bucket_range + 1
        bucket = [{'min':float("inf"), 'max':float("-inf")} for _ in range(bucket_count)]

        # Find the bucket where the n should be put.
        for n in nums:
            # min_val / max_val is in the first / last bucket.
            if n in (a, b):
                continue
            i = (n - a) // bucket_range
            bucket[i]['min'] = min(bucket[i]['min'], n)
            bucket[i]['max'] = max(bucket[i]['max'], n)

        # Count each bucket gap between the first and the last bucket.
        max_gap, pre_bucket_max = 0, a
        for i in range(bucket_count):
            # Skip the bucket it empty.
            if bucket[i]['min'] == float("inf") and bucket[i]['max'] == float("-inf"):
                continue
            max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
            pre_bucket_max = bucket[i]['max']
        # Count the last bucket.
        max_gap = max(max_gap, b - pre_bucket_max)

        return max_gap

    
