class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = []
        current_index_1 = 0
        current_index_2 = 0
        while True:
            if current_index_1 == m or current_index_2 == n:
                break
            if nums1[current_index_1] > nums2[current_index_2]:
                k.append(nums2[current_index_2])
                current_index_2 += 1
            else:
                k.append(nums1[current_index_1])
                current_index_1 += 1

        if current_index_1 == m:
            for i in range(current_index_2, n):
                k.append(nums2[i])

        if current_index_2 == n:
            for i in range(current_index_1, m):
                k.append(nums1[i])

        nums1[:] = k

