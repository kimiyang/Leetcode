class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxAchieve = [0,1,2,3,4,5,6]
        for i in range(7, N+1):
            max1 = maxAchieve[i-1] + 1
            max2 = 0
            for j in range(0, i-3):
                max2 = max(max2, maxAchieve[i-3-j]*(2+j))
            maxAchieve.append(max(max1, max2))
        return maxAchieve[N]
            
        
sol = Solution()
print sol.maxA(7)