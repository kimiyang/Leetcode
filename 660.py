class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        weight = 1
        while n > 0:
            left = n % 9
            res += weight * left
            n = n / 9
            weight *= 10
        return res