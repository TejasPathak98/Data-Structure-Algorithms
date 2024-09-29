class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals,key = lambda x : x[0])

        print(intervals)
        
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
        
        return result
