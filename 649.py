class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        current = senate
        n_d = 1
        n_r = 1
        while len(current) > 1 and n_d > 0 and n_r > 0:
            counter_r = 0
            counter_d = 0
            n_d = 0
            n_r = 0
            nextCurrent = ''
            temp = ''
            print current
            for s in current:
                if s == 'R':
                    if counter_r > 0:
                        counter_r -= 1
                    else:
                        temp += 'R'
                        counter_d += 1
                else:
                    if counter_d > 0:
                        counter_d -= 1
                    else:
                        temp += 'D'
                        counter_r += 1
            for s in temp:
                if s == 'R':
                    if counter_r > 0:
                        counter_r -= 1
                    else:
                        nextCurrent += 'R'
                        n_r += 1
                else:
                    if counter_d > 0:
                        counter_d -= 1
                    else:
                        nextCurrent += 'D'
                        n_d += 1
            current = nextCurrent
        if current[0] == 'R':
            return 'Radient'
        return 'Dire'
                




sol = Solution()
# print sol.predictPartyVictory("DRRDRDRDRDDRDRDR")
print sol.predictPartyVictory("DDRRRR")