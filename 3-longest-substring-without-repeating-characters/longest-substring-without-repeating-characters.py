class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}          # Stores the last index of each character
        left = 0          # Left boundary of the window
        ans = 0           # Length of the longest substring

        for right , char in enumerate(s):
            if char in dic and dic[char] >= left:
                left = dic[char]+1
            dic[char] = right
            ans = max(ans , right-left+1)
        return ans
    
            