# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1
        if not root:
            return 0
        q = Queue.Queue()
        q.put(root)
        qsize = 1
        show = 0
        while qsize > 0:
            row_width = 0
            empty_width = 0
            new_size = 0
            has_left = False
            # show += 1
            for i in range(0, qsize):
                c = q.get()
                if c.val == 'NIL':
                    if has_left:
                        empty_width += (c.left * 2)
                    row_width += c.left
                else:
                    row_width += 1
                    if c.left is None:
                        if has_left:
                            empty_width += 1
                    else:
                        has_left = True
                        if empty_width > 0:
                            node = TreeNode('NIL')
                            node.left = empty_width
                            q.put(node)
                            new_size += 1
                            empty_width = 0
                        q.put(c.left)
                        new_size += 1
                    if c.right is None:
                        if has_left:
                            empty_width += 1
                    else:
                        has_left = True
                        if empty_width > 0:
                            node = TreeNode('NIL')
                            node.left = empty_width
                            q.put(node)
                            new_size += 1
                            empty_width = 0
                        q.put(c.right)
                        new_size += 1
                    # if show == 6:
                    #     print str(c.val) + ' - ' + str(new_size)
                    #     print empty_width
            qsize = new_size
            # print new_size
            res = max(res, row_width)
        return res
                    
        
        