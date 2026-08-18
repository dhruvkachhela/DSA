class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        one = 0
        seen = {}
        res = 0
        for i in range( 0 , len(nums)):
            if nums[i]== 0:
                zero +=1
            else:
                one+=1
            
            diff = zero - one
            if diff == 0:
                res = max(res , i+1)
            if diff not in seen:
                seen[diff] = i
            else:
                index = seen[diff]
                lenth = i - index
                res = max(res , lenth)
        return res
