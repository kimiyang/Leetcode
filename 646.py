class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x:x[1])
        res = 0
        print pairs
        while len(pairs) > 0:
            res += 1
            p = pairs.pop(0)
            while len(pairs) > 0 and pairs[0][0] <= p[1]:
                pairs.pop(0)
        return res
sol = Solution()
print sol.findLongestChain([[1,2], [2,3], [3,4]])