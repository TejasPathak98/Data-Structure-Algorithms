class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals = sorted(intervals,key = lambda x : (x[0],x[1]))
        result = []
        result.append(intervals[0])

        i = 1


        while i < len(intervals):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
                i += 1
            elif intervals[i][0] <= result[-1][1]:
                entry = min(result[-1][0],intervals[i][0])
                the_exit = max(result[-1][1],intervals[i][1])
                result[-1][0] = entry
                result[-1][1] = the_exit
                i += 1

        return result
            

        