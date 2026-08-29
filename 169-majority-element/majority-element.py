class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thresold = len(nums)/2

        seen = {}

        for num in nums:
            seen[num]= seen.get(num,0) +1
            if seen.get(num,0)>thresold:
                return num
            
