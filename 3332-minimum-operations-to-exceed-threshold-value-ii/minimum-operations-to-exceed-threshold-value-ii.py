class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if all(x >= k for x in nums):
            return 0       

        heap = []
        for num in nums:
            heappush(heap, num)

        def Condition_checker(arr):
            return all(x >= k for x in arr)

        operations = 0
        
        while len(heap) >= 2:

            x = heappop(heap)
            y = heappop(heap)
            operations += 1

            heappush(heap, min(x, y) * 2 + max(x, y))

            if Condition_checker(heap):
                return operations
        

        return -1




