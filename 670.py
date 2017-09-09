class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nList = map(int, str(num))
        lastBigger = {x: i for i, x in enumerate(nList) }
        for i, x in enumerate(nList):
            for b in xrange(9, x, -1):
                if lastBigger.get(b, None) > i:
                    nList[i], nList[lastBigger[b]] = nList[lastBigger[b]], nList[i]
                    return int("".join(map(str, nList)))
        return num
                