class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0 
        n = len(arr)
        avg = 0 

        curr_sum = sum(arr[:k])
        avg = curr_sum / k
        if avg >= threshold:
            count += 1

        i = 0
        for j in range(k,n):
            curr_sum = curr_sum - arr[i] + arr[j]
            if curr_sum / k >= threshold:
                count += 1 
            i += 1

        return count
        
        