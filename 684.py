class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        seen = set()
        graph = {}
        def dfs(src, tar):
            if src in seen:
                return False
            seen.add(src)
            if src == tar:
                return True
            return any(dfs(neighbor, tar) for neighbor in graph[src])
        for (s, e) in edges:
            seen = set()
            if s in graph and e in graph and dfs(s, e):
                return [s, e]
            if s not in graph:
                graph[s] = []
            if e not in graph:
                graph[e] = []
            graph[s].append(e)
            graph[e].append(s)