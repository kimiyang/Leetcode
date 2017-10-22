class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nSet = set()
        times = time.split(':')
        hour = times[0]
        minute = times[1]
        hl = list(hour)
        ml = list(minute)
        hl[0] = int(hl[0])
        hl[1] = int(hl[1])
        ml[0] = int(ml[0])
        ml[1] = int(ml[1])
        if hl[0] == hl[1] == ml[0] == ml[1]:
            return time
        
        nSet.add(hl[0])
        nSet.add(hl[1])
        nSet.add(ml[0])
        nSet.add(ml[1])
        startTime = (hl[0] * 10 + hl[1]) * 3600 + (ml[0] * 10 + ml[1]) * 60
        diff = 86400
        res = ''
        for i in xrange(3):
            h1 = (hl[0] + i) % 3
            if h1 not in nSet:
                continue
            h2Range = 10
            if h1 == 2:
                h2Range = 4
            for j in xrange(h2Range):
                h2 = (hl[1] + j) % h2Range
                if h2 not in nSet:
                    continue
                for k in xrange(6):
                    m1 = (ml[0] + k) % 6
                    if m1 not in nSet:
                        continue
                    for l in xrange(10):
                        m2 = (ml[1] + l) % 10
                        if m2 not in nSet:
                            continue
                        endTime = (h1 * 10 + h2) * 3600 + (m1 * 10 + m2) * 60
                        if endTime == startTime:
                            continue
                        currentDiff = (endTime - startTime + 86400) % 86400
                        if currentDiff < diff:
                            diff = currentDiff
                            res = str(h1) + str(h2) + ":" + str(m1) + str(m2)
            return res
                        