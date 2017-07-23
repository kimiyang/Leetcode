class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        now_sum = 0
        for i in range(k):
            now_sum += nums[i]
        max_sum = now_sum
        for i in range(len(nums) - k):
            now_sum = now_sum - nums[i] + nums[i + k]
            if now_sum > max_sum:
                max_sum = now_sum
            print max_sum
        return max_sum * 1.0 / k



sol = Solution()
print sol.findMaxAverage([1,12,-5,-6,50,3,33,-10,98,54,-10,45], 5)