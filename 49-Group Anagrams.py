class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        res = []
        for l in hashmap.values():
            res.append(l)
        return res
