class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1,1]]
        nLen = len(nums)
        maxN = 1
        res = 0
        if nLen < 1:
            return 0
        for i in xrange(1, nLen):
            nLongest = 1
            count = 1
            for j in xrange(0, i):
                if nums[i] > nums[j]:
                    if nLongest < dp[j][0]+1:
                        count = dp[j][1]
                        nLongest = dp[j][0]+1
                    elif nLongest == dp[j][0]+1:
                        count += dp[j][1]
            maxN = max(maxN, nLongest)
            dp.append([nLongest, count])
            # print dp
        for i in xrange(0, len(dp)):
            if dp[i][0] == maxN:
                res += dp[i][1]
        return res
            