from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = set(nums1)
        total = []
        for num in nums2:
            if num in seen:
                total.append(num)
                seen.remove(num)
        return total
                