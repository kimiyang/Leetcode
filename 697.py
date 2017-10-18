class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        freq = 0
        res = 50000
        for pos, n in enumerate(nums):
            if n not in numMap:
                numMap[n] = {
                    "freq": 0,
                    "minPos": pos,
                    "maxPos": pos
                }
            numMap[n]["freq"] += 1
            numMap[n]["maxPos"] = pos
            if numMap[n]["freq"] > freq:
                res = numMap[n]["maxPos"] - numMap[n]["minPos"] + 1
            elif numMap[n]["freq"] == freq:
                res = min(numMap[n]["maxPos"] - numMap[n]["minPos"] + 1, res)
            freq = max(freq, numMap[n]["freq"])
        return res
            