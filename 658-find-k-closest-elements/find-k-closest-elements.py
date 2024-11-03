class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0 
        high = len(arr) - k

        while low < high:
            mid = (low + high) // 2
            if x <= arr[mid]:
                high = mid
            elif x >= arr[mid + k]:
                low = mid + 1
            else:
                d1 = abs(x - arr[mid])
                d2 = abs(x - arr[mid + k])
                if d1 <= d2:
                    high = mid
                else:
                    low = mid + 1
            
        return arr[low:low + k]
        