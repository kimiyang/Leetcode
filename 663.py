# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTotalVal(self, root):
        if root is None:
            return 0
        return root.val + self.getTotalVal(root.left) + self.getTotalVal(root.right)
    def postOrderCheck(self, root, total_val):
        if root is None:
            return ['NIL', False]
        left_val = 0
        right_val = 0
        left = self.postOrderCheck(root.left, total_val)
        if left[1] or (left[0] != 'NIL' and left[0] * 2 == total_val):
            return [0, True]
        right = self.postOrderCheck(root.right, total_val)
        if right[1] or (right[0] != 'NIL' and right[0] * 2 == total_val):
            return [0, True]
        if left[0] != 'NIL':
            left_val = left[0]
        if right[0] != 'NIL':
            right_val = right[0]
        return [left_val + right_val + root.val, False]
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        total_val = self.getTotalVal(root)
        return self.postOrderCheck(root, total_val)[1]
        