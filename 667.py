class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [i for i in range(1, n+1)]
        diff = k
        for i in range(0, k):
            res[n-k+i] = res[n-k+i-1]+diff
            if diff < 0:
                diff = -diff-1
            else:
                diff = -(diff-1)
        return res
            
        