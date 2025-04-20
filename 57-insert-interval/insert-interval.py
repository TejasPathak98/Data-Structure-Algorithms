class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
        
        if newInterval:
            result.append(newInterval)
        
        return result
