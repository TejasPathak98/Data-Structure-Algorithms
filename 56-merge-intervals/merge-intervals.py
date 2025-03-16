class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        prev_end_time = float("-inf")

        for i in range(len(intervals)):
            if intervals[i][0] > prev_end_time:
                ans.append(intervals[i])
            else:
                ans[-1][0] = min(ans[-1][0],intervals[i][0])
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            prev_end_time = ans[-1][1]

        return ans
            

