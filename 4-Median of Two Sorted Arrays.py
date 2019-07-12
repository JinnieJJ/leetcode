class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l//2)
        else:
            return (self.kth(nums1, nums2, l//2)+self.kth(nums1, nums2, l//2-1)) / 2.0
    
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        
        if ia + ib < k:
            if ma > mb:
                return self.kth(a, b[ib+1:], k-ib-1)
            else:
                return self.kth(a[ia+1:], b, k-ia-1)
        else:
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        imin = 0
        imax = m
        halfLen = (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = halfLen - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                print(i)
                if i == 0:
                    maxOfLeft = nums2[j-1]
                elif j == 0:
                    maxOfLeft = nums1[i-1]
                else:
                    maxOfLeft = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return maxOfLeft
                
                if i == m:
                    minOfRight = nums2[j]
                elif j == n:
                    minOfRight = nums1[i]
                else:
                    minOfRight = min(nums1[i], nums2[j])
                
                return (maxOfLeft + minOfRight) / 2.0
