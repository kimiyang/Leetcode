# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    nodeSet = set()
    codeMap = {}
    res = []
    def postTraversal(self, root):
        if root is None:
            return '^'
        leftCode = self.postTraversal(root.left)
        rightCode = self.postTraversal(root.right)
        code = str(root.val) + leftCode + rightCode
        if code not in self.codeMap:
            if code in self.nodeSet:
                self.res.append(root)
                self.codeMap[code] = root
            else:
                self.nodeSet.add(code)
        return code
        
    
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.res = []
        self.nodeSet = set()
        self.codeMap = {}
        self.postTraversal(root)
        return self.res
        
        