# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructTree(self, nums, left, right):
        if left > right:
            return None
        max_n = nums[left]
        index = left
        for i in range(left, right+1):
            if max_n < nums[i]:
                max_n = nums[i]
                index = i
        root = TreeNode(max_n)
        root.left = self.constructTree(nums, left, index-1)
        root.right = self.constructTree(nums, index+1, right)
        return root
        
        
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(nums, 0, len(nums)-1)
        
            