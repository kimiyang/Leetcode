class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row_size = len(M)
        if row_size < 1:
            return []
        col_size = len(M[0])
        res = []
        for i in range(0, row_size):
            row = []
            for j in range(0, col_size):
                counter = 1
                val_sum = M[i][j]
                if i > 0:
                    val_sum += M[i-1][j]
                    counter += 1
                    if j > 0:
                        val_sum += M[i-1][j-1]
                        counter += 1
                    if j < col_size - 1:
                        val_sum += M[i-1][j+1]
                        counter += 1
                if i < row_size - 1:
                    val_sum += M[i+1][j]
                    counter += 1
                    if j > 0:
                        val_sum += M[i+1][j-1]
                        counter += 1
                    if j < col_size - 1:
                        val_sum += M[i+1][j+1]
                        counter += 1
                if j > 0:
                    val_sum += M[i][j-1]
                    counter += 1
                if j < col_size - 1:
                    val_sum += M[i][j+1]
                    counter += 1
                row.append(val_sum / counter)
            res.append(row)
        return res
            