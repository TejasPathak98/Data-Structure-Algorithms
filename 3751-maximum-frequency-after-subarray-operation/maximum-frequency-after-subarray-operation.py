class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_freq = 0
        count_k = nums.count(k) # we are counting the existing k values

        for target in range(1,51):
            if target == k:
                continue

            current_gain = 0
            max_gain = 0

            for num in nums:
                if num == target:
                    current_gain += 1
                elif num == k:
                    current_gain -= 1
                else:
                    continue
                

                max_gain = max(max_gain,current_gain)

                if current_gain < 0:
                    current_gain = 0

            
            max_freq = max(max_freq,max_gain)

        
        return max_freq + count_k