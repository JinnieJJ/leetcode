class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) < W:
            return False
        
        handDict = collections.Counter(hand)
        while handDict:
            minhand = min(handDict.keys())
            for y in range(minhand, minhand + W):
                if not handDict[y]:
                    return False
                handDict[y] -= 1
                if handDict[y] == 0:
                    del handDict[y]
        return True
