class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        t = ""
        for i in range(len(s)-1 , -1 ,-1):
            if i == 0:
                t += s[i]
            else:
                t += s[i] + " "
        return t
        
