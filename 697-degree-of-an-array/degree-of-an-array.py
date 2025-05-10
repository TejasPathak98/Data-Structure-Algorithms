class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = max(counter.values())

        elements = []

        for key,value in counter.items():
            if value == max_freq:
                elements.append(key)
        
        min_length = float('inf')

        for x in elements:
            right = 0
            left = 0
            n = len(nums)
            first_occ = False
            count = 0

            while right < n:

                if nums[right] == x:
                    if not first_occ:
                        left = right
                        first_occ = True
                    count += 1
                    if count == max_freq:
                        min_length = min(min_length,right - left + 1)
                        break

                right += 1

        
        return min_length
                    

                




