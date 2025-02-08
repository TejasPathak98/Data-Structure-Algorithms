class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        res = float("-inf")

        for interval in sorted(intervals,key = lambda x : x[1]):
            if interval[0] >= res:
                res = interval[1]
            else:
                ans += 1
        
        return ans
        