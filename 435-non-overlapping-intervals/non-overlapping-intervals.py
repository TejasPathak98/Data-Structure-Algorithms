class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort by the End Time

        intervals.sort(key = lambda x : x[1])
        prev_meeting_end = float("-inf")
        ans = 0

        for i in range(len(intervals)):
            if intervals[i][0] >= prev_meeting_end:
                prev_meeting_end = intervals[i][1]
            else:
                ans += 1
        
        return ans
        