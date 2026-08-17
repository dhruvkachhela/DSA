class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        seen = {0:1}
        ans = 0

        for i in range(0 , len(nums)):
            total += nums[i]
            rem = total % k
            if rem <0:
                rem = rem +k
            ans += seen.get(rem , 0)
            seen[rem] = seen.get(rem , 0) +1
        return ans