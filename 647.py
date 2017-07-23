class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        res = length
        prev_set1 = set(i for i in range(0, length))
        prev_set2 = set()
        for i in range(2, length+1):
            new_set = set()
            for j in range(0, length - i + 1):
                is_in_set = False
                if i % 2 == 0:
                    is_in_set = (j+1) in prev_set2
                else:
                    is_in_set = (j+1) in prev_set1
                if s[j] == s[j+i-1] and (i == 2 or is_in_set):
                    res += 1
                    new_set.add(j)
            if i % 2 == 0:
                prev_set2 = new_set
            else:
                prev_set1 = new_set
        return res
                    
sol = Solution()
print sol.countSubstrings("leede")