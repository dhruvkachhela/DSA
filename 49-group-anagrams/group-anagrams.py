from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mapping[key].append(word)
        return list(mapping.values())