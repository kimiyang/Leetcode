#!/usr/bin/env python
import sys

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nLen = len(nums)
        if nLen < 3:
            return True
        temp = [[0 for i in range(nLen + 1)] for j in range(nLen - 2)]
        tempTotal = [[0 for i in range(nLen + 1)] for j in range(nLen)]
        print temp
        for i in range(3, nLen + 1):
            for j in range(0, nLen - i + 1):
                print 'i = ' + str(i) + ' j = ' + str(j)
                maxSum = 0
                total = 0
                if i == 3:
                    maxSum = max(nums[j]+min(nums[j+1], nums[j+2]), nums[j+2] + min(nums[j], nums[j+1]))
                    total = nums[j] + nums[j+1] + nums[j+2]
                else:
                    maxSum = max(nums[j] + tempTotal[j+1][i-1] - temp[j+1][i-1], nums[j + i - 1] + tempTotal[j][i-1] - temp[j][i-1])
                    total = nums[j] + tempTotal[j+1][i-1]
                temp[j][i] = maxSum
                tempTotal[j][i] = total
                print maxSum
        maxTotal = temp[0][nLen]
        print temp
        print tempTotal
        return maxTotal >= tempTotal[0][nLen] - maxTotal




if __name__ == "__main__":
    sol = Solution()
    print sol.PredictTheWinner([33,44,55,66,77,88,99,11,22])
