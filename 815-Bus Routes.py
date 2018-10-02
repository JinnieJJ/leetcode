class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        busClassifier = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                busClassifier[stop].add(bus)
        busNext = collections.defaultdict(set)
        for buses in busClassifier.values():
            for bus in buses:
                busNext[bus] |= set(buses)
        
        q = busClassifier[S] #站S的所有车
        visited = set(q)
        found = False
        ans = 0
        while q and not found:
            q0 = []
            for bus in q:
                if bus in busClassifier[T]: #其中有到站T的车
                    found = True
                    break
                for nbus in busNext[bus]:
                    if nbus not in visited:
                        q0.append(nbus)
                        visited.add(nbus)
            q = q0
            ans += 1
        return ans if found else -1
