# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left == '':
            if right == '':
                return str(t.val)    
            return str(t.val) + '()(' + str(right) + ')'
        if right == '':
            return str(t.val) + '(' + str(left) + ')'
        return str(t.val) + '(' + str(left) + ')(' + str(right) + ')'