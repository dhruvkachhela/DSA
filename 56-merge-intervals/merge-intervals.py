class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = [intervals[0]]

        for start, end in intervals:
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1] , end)
            else:
                ans.append([start , end])
        return ans
        
        # if not a:
        # return []

    # res = []
    # intevals.sort()  # Sorts intervals by start time, then end time

    # start = a[0][0]
    # end = a[0][1]

    # for i in range(1, len(a)):
    #     s = intervals[i][0]
    #     e = interva;s[i][1]

    #     if end >= s:  # Overlap
    #         end = max(end, e)
    #         continue

    #     # No overlap -> save the current interval and start a new one
    #     res.append([start, end])
    #     start = s
    #     end = e

    # # Append the last merged interval
    # res.append([start, end])
    # return res  
