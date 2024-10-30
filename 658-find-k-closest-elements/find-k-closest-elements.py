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
                d1 = abs(arr[mid] - x)
                d2 = abs(arr[mid + k] - x)
                if d1 <= d2:
                    high = mid
                else:
                    low = mid + 1
        
        return arr[low:low + k]