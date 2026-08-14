class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = min_sum = nums[0]
        res = abs(nums[0])

        for i in range( 1 , len(nums)):
            max_sum = max( max_sum + nums[i] , nums[i])
            min_sum = min( min_sum + nums[i] , nums[i])
            res = max(res, max(abs(min_sum) , max_sum))
        return res