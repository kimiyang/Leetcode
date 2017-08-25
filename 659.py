class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible = {}
        current = {}
        counter = 0
        for n in nums:
            if n-1 in current and current[n-1][0] > 0:
                current[n-1][0] -= 1
                if current[n-1][1] == 2:
                    if n in possible:
                        possible[n] += 1
                    else:
                        possible[n] = 1
                    counter -= 1
                else:
                    if n in current:
                        current[n][0] += 1
                    else:
                        current[n] = [1, current[n-1][1] + 1]
                    
            elif n-1 in possible and possible[n-1] > 0:
                possible[n-1] -= 1
                if n in possible:
                    possible[n] += 1
                else:
                    possible[n] = 1
            else:
                if n in current:
                    current[n][0] += 1
                else:
                    current[n] = [1, 1]
                counter += 1
            # print current
        # print stack
        return counter < 1
                
                
                