class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        prev_end_time = float("-inf")

        for i in range(len(intervals)):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])

        return ans

        #O(NlogN) ;O(1)
            

