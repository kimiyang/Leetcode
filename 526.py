class Solution(object):
    def countBeautiful(self, arr, offset, len_arr):
        if len_arr == 1:
            if arr[0] % offset == 0 or offset % arr[0] == 0:
                return 1
            return 0
        res = 0
        for i in xrange(0, len_arr):
            if offset % arr[i] == 0 or arr[i] % offset == 0:
                temp = arr[0]
                arr[0] = arr[i]
                arr[i] = temp
                res += self.countBeautiful(arr[1:], offset+1, len_arr-1)
                arr[i] = arr[0]
                arr[0] = temp
        return res
        
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        arr = []
        for i in range(0, N):
            arr.append(i+1)
        return self.countBeautiful(arr, 1, N)