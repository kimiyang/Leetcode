class Solution(object):
    def minSteps(self, n):
        prev = [0, 2]
        minStep = 100000
        for i in range (3, n+1):
            minStep = i
            print "i=" + str(i)
            for j in range(i/2+1, 1, -1):
                print j
                if i % j == 0:
                    step = prev[j-1] + i/j
                    if step < minStep:
                        minStep = step
            prev.append(minStep)
        return minStep

sol = Solution()
print sol.minSteps(36)