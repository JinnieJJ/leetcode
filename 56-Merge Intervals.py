# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        
        for interval in intervals:
            current = result[-1]
            if interval.start <= current.end:
                current.end = max(interval.end, current.end) # pass by reference
            else:
                result.append(interval)
        return result

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class TreeNode:
    def __init__(self, start, end, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = None
    
    def p(self, root, res):
        if root:
            self.p(root.left, res)
            res.append(Interval(root.start, root.end))
            self.p(root.right, res)
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda interval:(interval.start, interval.end))
        
        for interval in intervals:
            if not self.root:
                self.root = TreeNode(interval.start, interval.end)
            else:
                self.add(self.root, interval)
        res = []
        self.p(self.root, res)
        return res
        
    def add(self, root, interval):
        if not root:
            return TreeNode(interval.start, interval.end)
        
        if interval.end < root.start:
            root.left = self.add(root.left, interval)
        elif interval.start > root.end:
            root.right = self.add(root.right, interval)
        else: # overlap
            root.start = min(root.start, interval.start)
            root.end = max(root.end, interval.end)
            
            # check for the unoverlapped right and left
            l_node = root.left
            while l_node and l_node.end >= root.start:
                root.start = min(root.start, l_node.start)
                l_node = l_node.left
            r_node = root.right
            while r_node and r_node.start <= root.end:
                root.end = max(root.end, r_node.end)
                r_node = r_node.right
            root.left = l_node
            root.right = r_node
        return root
