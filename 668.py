class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left = 1
        right = m * n
        while left < right:
            count = 0
            self_count = 0
            mid = (left+right)/2
            for i in range(1, m+1):
                div = mid / i
                if div <= n:
                    if mid % i == 0:
                        count -= 1
                        self_count += 1
                    count += div
                else:
                    count += n
            if count < k:
                if count + self_count >= k:
                    return mid
                left = mid+1
            else:
                right = mid-1
        return left