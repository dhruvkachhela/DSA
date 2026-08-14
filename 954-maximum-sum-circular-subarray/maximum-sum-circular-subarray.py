class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max_res = nums[0]
        min_sum = min_res = nums[0]
        total_sum = sum(nums)

        for i in range(1, len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            max_res = max(max_res, max_sum)

            min_sum = min(min_sum + nums[i], nums[i])
            min_res = min(min_res, min_sum)

        if min_res == total_sum:
            return max_res

        return max(max_res, total_sum - min_res)