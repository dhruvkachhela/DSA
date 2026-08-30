from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            seen= {}
            seen= Counter(s)

            for char in t:
                if char not in seen:
                    return False
                seen[char] -=1

                if seen[char] ==0:
                    del seen[char]
            return True

        else:
            return False


        