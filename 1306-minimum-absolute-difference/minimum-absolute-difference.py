class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_diff = float('inf')

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < min_diff:
                min_diff = abs(arr[i] - arr[i + 1])
                result.clear()
                fe = min(arr[i],arr[i + 1])
                se = max(arr[i],arr[i + 1])
                result.append([fe,se])
            elif abs(arr[i] - arr[i + 1]) == min_diff:
                fe = min(arr[i],arr[i + 1])
                se = max(arr[i],arr[i + 1])
                result.append([fe,se])

        return result
            
            

