class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = {}
        group = {}
        res = []
        maxCount = 0
        resCount = 0
        for w in words:
            if w not in freq:
                freq[w] = 0
            freq[w] += 1
            maxCount = max(maxCount, freq[w])
        for key,val in freq.iteritems():
            if val not in group:
                group[val] = []
            group[val].append([key,val])
        for i in xrange(maxCount, 0, -1):
            if i in group and resCount < k:
                res.extend(group[i])
                resCount += len(group[i])
        res.sort(cmp = lambda a, b: b[1] - a[1] if a[1] != b[1] else (-1 if a[0] < b[0] else 1))
        return [ele[0] for ele in res[:k]]
        