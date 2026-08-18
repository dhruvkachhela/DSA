class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        one = 0
        seen = {0 : -1}
        res = 0
        for i in range( 0 , len(nums)):
            if nums[i]== 0:
                zero +=1
            else:
                one+=1
            
            diff = zero - one
            if diff in seen:
                res = max(res, i - seen[diff])
            else:
                seen[diff] = i
        return res
