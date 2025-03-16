class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals,key = lambda x : x[0])

        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        
        return True

        #(ONlogN) ; O(N) -> We can make SC O(1) by using .sort()