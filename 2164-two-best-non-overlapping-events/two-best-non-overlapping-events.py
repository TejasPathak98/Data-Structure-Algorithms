class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        heap = []
        result = 0
        maxValue = 0
        events.sort()

        for start,end,value in events:
            while heap and heap[0][0] < start:
                maxValue = max(maxValue,heappop(heap)[1])
            result = max(result,maxValue + value)
            heappush(heap, (end,value))

        return result


