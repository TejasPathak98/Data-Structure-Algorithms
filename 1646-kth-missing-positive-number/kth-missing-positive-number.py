class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        index = 0
        current_number = 1

        while index < len(arr):
            if arr[index] != current_number:
                missing_count += 1

                if missing_count == k:
                    return current_number

            else:
                index += 1
            
            current_number += 1
        
        while missing_count <= k:
            current_number += 1
            missing_count += 1
            if missing_count == k:
                return current_number - 1
        
        


        
        