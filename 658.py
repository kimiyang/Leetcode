class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0
        low = 0
        r = len(arr) - 1
        mid = (l + r) / 2
        while l < r:
            mid = (l + r) / 2
            if arr[mid] > x:
                r = mid
            else:
                l = mid + 1
        if mid + 1 < len(arr) and abs(arr[mid+1]) - x < abs(x-arr[mid]):
            mid = mid + 1
        low = mid
        l = mid - 1
        r = mid + 1
        # print 'mid=' + str(mid)
        for i in range(0, k-1):
            # print 'l=' + str(l) + ' r=' + str(r)
            if l < 0:
                r += 1
                low = 0
            elif r >= len(arr):
                low = l
                l -= 1
            elif abs(x-arr[l]) <= abs(arr[r]-x):
                low = l
                l -= 1
            else:
                r += 1
        # print low
        return arr[low:low+k]
                