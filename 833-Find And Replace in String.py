class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        bucket = [None] * len(S)
        for i in range(len(indexes)):
            if indexes[i] + len(sources[i]) <= len(S) and S[indexes[i]:indexes[i]+len(sources[i])] == sources[i]:
                bucket[indexes[i]] = (len(sources[i]), list(targets[i]))
                # print(bucket)
        result = []
        S = list(S)
        last = 0
        for i in range(len(S)):
            if bucket[i]:
                result.extend(bucket[i][1])
                last = i + bucket[i][0]
            elif i >= last:
                result.append(S[i])
        return "".join(result)
