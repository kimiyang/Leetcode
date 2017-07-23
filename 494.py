#!/usr/bin/env python
import sys

class Solution(object):

     def helper(self, nums, S, map):
         res = 0
         index = len(nums) - 1
         if S in map[index]:
             return map[index][S]
         if len(nums) == 1:
             if nums[0] == S and -nums[0] == S:
                 res = 2
             elif nums[0] == S or -nums[0] == S:
                 res = 1
             else:
                 res = 0
             map[index][S] = res
             return res

         res = self.helper(nums[:-1], S+nums[-1], map) + self.helper(nums[:-1], S-nums[-1], map)
         map[index][S] = res
         return res

     def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.map = [dict() for i in range(len(nums))]
        return self.helper(nums,S,self.map)



if __name__ == "__main__":
    sol = Solution()
    print sol.findTargetSumWays([0,0],0)
    print sol.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)
    print sol.findTargetSumWays([1,2,3,4,5,6,7],7)
    # print Solution.map
