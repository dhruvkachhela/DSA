class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        curr = 1
        
        for _ in range(n):
            result.append(curr)
            
            if curr * 10 <= n:               # can go deeper → append a 0
                curr *= 10
            else:
                # cannot go deeper → need the next sibling (or uncle, etc.)
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10              # backtrack
                curr += 1                    # move to next number
        
        return result

        