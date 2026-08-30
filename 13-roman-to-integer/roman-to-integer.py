class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = { "I"       :        1,
                    "V"      :        5,
                    "X"      :        10,
                    "L"      :        50,
                    "C"      :        100,
                    "D"      :        500,
                    "M"      :        1000}
        final = 0
        for i , rom in enumerate(s):
            if i == len(s)-1:
                final = final + mapping.get(s[i],0)
            elif mapping[s[i]] < mapping[s[i+1]]:
                final = final - mapping[s[i]]
            else:
                final = final + mapping[s[i]]
        return final 
