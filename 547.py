class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        R = [10000 for n in range(len(M))]
        res = 0
        resSet = set()
        for i in range(0, len(M)):
            if(R[i] == 10000):
                res = R[i] = res + 1
                resSet.add(R[i])
            for j in range(i+1, len(M[i])):
                if M[i][j] == 1:
                    if R[i] < R[j] and R[j] in resSet:
                        resSet.remove(R[j])
                    elif R[i] > R[j] and R[i] in resSet:
                        resSet.remove(R[i])
                    R[j] = R[i] = min(R[i], R[j])
        return len(resSet)


sol = Solution()
sol.findCircleNum( [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
 [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
 [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
 [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
 [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
 [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
 [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
 [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
)