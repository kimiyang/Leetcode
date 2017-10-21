class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort(reverse=True)
        totSum = sum(nums)
        if totSum % k > 0:
            return False
        avg = totSum / k
        def dfs(nums, target, n, step, k):
            if step == k:
                return True
            for i in xrange(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                if n + nums[i] == target:
                    if dfs(newNums, target, 0, step+1, k):
                        return True
                elif n + nums[i] < target:
                    if dfs(newNums, target, n+nums[i], step, k):
                        return True
                elif n == 0:
                    return False
            return False
        return dfs(nums, avg, 0, 1, k)
        
        