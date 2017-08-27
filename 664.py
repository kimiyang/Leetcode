class Solution(object):
    res_map = {}
    def helper(self, s, i, j):
        if j - i < 0:
            return 0
        if i == j:
            return 1

        if (i,j) in self.res_map:
            return self.res_map[(i,j)]
        best = self.helper(s, i+1, j) + 1
        for k in xrange(i+1, j+1):
            if s[k] == s[i]:
                best = min(self.helper(s, i, k-1) +  self.helper(s, k+1, j), best)
        self.res_map[(i,j)] = best
        return best
        
        
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res_map = {}
        return self.helper(s, 0, len(s) - 1)