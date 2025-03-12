class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while stones and len(stones) >= 2:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones, -1 *(y - x))
        
        if stones and len(stones) > 0:
            return -stones[0]
        
        return 0

        # heapq.heapify(stones) does not return anything