class Solution(object):
    
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = {}
        def findRoot(word):
            res = ''
            t = trie
            for w in word:
                if w in t:
                    res += w
                    t = t[w]
                    if '#' in t:
                        return res 
                else:
                    return word
            return word
        
        res = ''
        for w in dict:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
            
        return " ".join(map(findRoot, sentence.split()))
    
         


sol = Solution()
print sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")