class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(0, len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
        
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i+1]
        return res
        


sol = Solution()
print sol.findErrorNums([5,1,3,4,6,7,9,10,8,6])