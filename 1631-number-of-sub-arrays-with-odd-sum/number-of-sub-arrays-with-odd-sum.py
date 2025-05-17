class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        odd_count = 0
        MOD = 10**9 + 7
        prefix_sum = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 1:
                odd_count += 1

        even_count = len(arr) - odd_count

        return (odd_count + (odd_count * even_count)) % MOD

    