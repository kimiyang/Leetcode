class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        equalPosMap = {0: -1}
        counter = 0
        res = 0
        for x, i in enumerate(nums):
            counter -= 1 if i == 0 else -1
            if counter in equalPosMap:
                res = max(res, x - equalPosMap[counter])
            else:
                equalPosMap[counter] = x
        return res
            