#!/usr/bin/env python
import sys

class Solution(object):
    def findComplement(self, num):
        """
        :type nums: List[int]
        :rtype: bool
        """
        re = 0
        for i in bin(num)[2:]:
            re = re << 1
            if(i == '0'):
                re = re | 1
        return re



if __name__ == "__main__":
    sol = Solution()
    print sol.findComplement(1)
