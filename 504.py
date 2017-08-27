class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = 0
        weight = 1
        f = 1
        if num < 0:
            f = -1
            num = -num
        while num > 0:
            left = num % 7
            res += weight * left
            num = num / 7
            weight *= 10
        return str(res * f)