# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return 0
        node_list = [root]
        res = []
        num = 1
        while len(node_list) > 0:
            avg = 0
            count = num
            num = 0
            for i in range (0, count):
                first_ele = node_list.pop(0)
                avg += first_ele.val
                if first_ele.left:
                    node_list.append(first_ele.left)
                    num += 1
                if first_ele.right:
                    node_list.append(first_ele.right)
                    num += 1
            avg = avg*1.0 / count
            res.append(avg)
        return res
        