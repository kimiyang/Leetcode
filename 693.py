class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = n % 2
        while n > 0:
            n = n / 2
            if flag == n % 2:
                return False
            flag = flag ^ 1
        return True