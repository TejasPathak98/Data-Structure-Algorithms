class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = float(-inf)

        for i in range(1,len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance,abs(smallest - arr[-1]), abs(biggest - arr[0]))
            smallest = min(smallest,arr[0])
            biggest = max(biggest,arr[-1])
        
        return max_distance
        