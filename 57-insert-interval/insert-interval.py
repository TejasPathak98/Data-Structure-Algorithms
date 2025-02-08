class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            else:
                start = min(interval[0],newInterval[0])
                end = max(interval[1],newInterval[1])
                newInterval[0] = start
                newInterval[1] = end

        result.append(newInterval)
        return result