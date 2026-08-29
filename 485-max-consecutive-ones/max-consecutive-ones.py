class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        max_length= 0
        while right < len(nums):
            if nums[right] == 1:
                right+=1
                max_length = max(max_length , right-left +1)
            else:
                left = right +1
                right +=1
        if max_length <1:
            return 0
        return max_length-1
         

            
