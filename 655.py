# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        res = []
        h = self.getHeight(root)
        n = pow(2, h) - 1
        q = [root]
        for i in range(0, h):
            lvl = [''] * n
            count = pow(2, i)
            for j in range(0, count):
                top = q.pop(0)
                pos = j * (n / count + 1) + n / count / 2
                val = ''
                left = None
                right = None
                if top is not None:
                    val = str(top.val)
                    left = top.left
                    right = top.right
                lvl[pos] = val
                q.append(left)
                q.append(right)
            res.append(lvl)
        return res
        