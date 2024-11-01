class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if newInterval[0] > interval[1]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            else:
                st = min(newInterval[0],interval[0])
                ed = max(newInterval[1],interval[1])
                newInterval[0] = st
                newInterval[1] = ed

        result.append(newInterval)
        return result
        