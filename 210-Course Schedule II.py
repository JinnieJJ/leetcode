class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degrees = [0] * numCourses
        children = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1
            children[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True
        ans = []
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in children[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            for x in removeList:
                ans.append(x)
                courses.remove(x)
        if len(courses) == 0:
            return ans
        return []
