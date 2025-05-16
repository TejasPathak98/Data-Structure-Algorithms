class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        max_heap = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                heappush(max_heap, -matrix[i][j])

                if len(max_heap) > k:
                    heappop(max_heap)

        
        return -max_heap[0]