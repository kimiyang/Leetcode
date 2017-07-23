#!/usr/bin/env python
import sys

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        stack = [nums[0]]
        minStack = [nums[0]]
        minVal = nums[0]
        for c in nums:
            minVal = c
            while len(stack) > 0 and c >= stack[-1]:
                minVal = min(minStack[-1], minVal)
                print "pop min value: " + str(minVal) + " pop: " + str(stack[-1]) + " min: " + str(minStack[-1])
                stack.pop()
                minStack.pop()
            if len(stack) > 0 and c < stack[-1] and len(minStack) > 0 and c > minStack[-1]:
                return True
            else:
                minStack.append(minVal)
                stack.append(c)
                print "append: " + str(c) + " minval: " + str(minVal)
        return False
        
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = bin(x ^ y)[2:]
        return z.count('1')


if __name__ == "__main__":
    sol = Solution()
    print sol.hammingDistance(2,4)
