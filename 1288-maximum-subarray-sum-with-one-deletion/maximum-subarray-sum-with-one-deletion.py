class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nodelete = arr[0]
        onedelete = float('-inf')
        res = nodelete

        for i in range ( 1 , len(arr)):
            prev_nodelete = nodelete
            prev_onedelete = onedelete

            nodelete = max(nodelete + arr[i] , arr[i])

            if prev_onedelete == float('-inf'):
                prev_onedelete = arr[i]
            else:
                prev_onedelete = prev_onedelete + arr[i]

            onedelete = max(prev_onedelete , prev_nodelete)
            res = max(res , max(onedelete , nodelete))

        return res