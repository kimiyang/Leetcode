class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0]*26
        for t in tasks:
            count[ord(t)-ord('A')] += 1
        count.sort(lambda a, b: cmp(a,b))
        i = 25
        while i >= 0 and count[i] == count[25]:
            i -= 1
        return max((count[25] - 1) * (n + 1) + 25 - i, len(tasks))
        