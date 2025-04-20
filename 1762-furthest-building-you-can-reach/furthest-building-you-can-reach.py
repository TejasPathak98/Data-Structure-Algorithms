class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        

        diff = []
        i = 0

        while i < len(heights) - 1:

            if heights[i] >= heights[i + 1]:
                i += 1
                continue
            else:
                heapq.heappush(diff,(heights[i + 1] - heights[i]))
                if ladders > 0:
                    ladders -= 1
                else:
                    bricks -= heapq.heappop(diff)

                    if bricks < 0:
                        return i
                i += 1


        
        return len(heights) - 1
