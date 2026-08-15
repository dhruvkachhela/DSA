class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_ = sum(nums)
        left = 0
        if sum_ - nums[0]==0:
            return 0
        for i in range( 1 , n):
           left += nums[i-1]
           right = sum_ - left - nums[i]

           if right == left:
            return i
        return -1