class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        res = float("-inf")

        for interval in sorted(intervals,key = lambda x : x[0]):
            if interval[0] >= res:
                res = interval[1]
            else:
                return False
        
        return True

        