# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    node_map = set()
    def DFS(self, root, k):
        if not root:
            return False
        if (k-root.val) in self.node_map:
            return True
        self.node_map.add(root.val)
        return self.DFS(root.left, k) or self.DFS(root.right, k)
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.node_map = set()
        return self.DFS(root, k)