start, end, height = 0, 1, 2

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = self.ComputeSkylineInInterval(buildings, 0, len(buildings))

        res = []
        last_end = -1
        for interval in intervals:
            if last_end != -1 and last_end < interval[start]:
                res.append([last_end, 0])
            res.append([interval[start], interval[height]])
            last_end = interval[end]
        if last_end != -1:
            res.append([last_end, 0])

        return res

    # Divide and Conquer.
    def ComputeSkylineInInterval(self, buildings, left_endpoint, right_endpoint):
        if right_endpoint - left_endpoint <= 1:
            return buildings[left_endpoint:right_endpoint]
        mid = left_endpoint + ((right_endpoint - left_endpoint) // 2)
        left_skyline = self.ComputeSkylineInInterval(buildings, left_endpoint, mid)
        right_skyline = self.ComputeSkylineInInterval(buildings, mid, right_endpoint)
        return self.MergeSkylines(left_skyline, right_skyline)

    # Merge Sort.
    def MergeSkylines(self, left_skyline, right_skyline):
        i, j = 0, 0
        merged = []

        while i < len(left_skyline) and j < len(right_skyline):
            if left_skyline[i][end] < right_skyline[j][start]:
                merged.append(left_skyline[i])
                i += 1
            elif right_skyline[j][end] < left_skyline[i][start]:
                merged.append(right_skyline[j])
                j += 1
            elif left_skyline[i][start] <= right_skyline[j][start]:
                i, j = self.MergeIntersectSkylines(merged, left_skyline[i], i, right_skyline[j], j)
            else: # left_skyline[i][start] > right_skyline[j][start].
                j, i = self.MergeIntersectSkylines(merged, right_skyline[j], j, left_skyline[i], i)

        # Insert the remaining skylines.
        merged += left_skyline[i:]
        merged += right_skyline[j:]
        return merged

    # a[start] <= b[start]
    def MergeIntersectSkylines(self, merged, a, a_idx, b, b_idx):
        if a[end] <= b[end]:
            if a[height] > b[height]:   # a高
                if b[end] != a[end]:    # a占了全部 旁边多出b
                    b[start] = a[end]
                    merged.append(a)
                    a_idx += 1
                else:   # a完全遮住了b
                    b_idx += 1
            elif a[height] == b[height]:  # a和b一样高
                b[start] = a[start]
                a_idx += 1
            else:  # b高
                if a[start] != b[start]:    # a的后半部分被b挡住了
                    merged.append([a[start], b[start], a[height]])
                a_idx += 1
        else:  # a[end] > b[end]
            if a[height] >= b[height]:  # a把b完全遮住了
                b_idx += 1
            else:   # b中间部分搞出来
                if a[start] != b[start]:
                    merged.append([a[start], b[start], a[height]])
                a[start] = b[end]
                merged.append(b)
                b_idx += 1
        return a_idx, b_idx
