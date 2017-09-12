class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        for i in xrange(0, len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                count += 1
                res = max(count, res)
            else:
                count = 1
        return res