class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque() #monotonically decreasing
        min_deque = deque() #monotonically increasing

        j = 0
        max_len = float('-inf')

        
        for i in range(len(nums)):

            while max_deque and nums[i] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[i])

            while min_deque and nums[i] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[i])

            while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:

                if nums[j] == max_deque[0]:
                    max_deque.popleft()
                
                if nums[j] == min_deque[0]:
                    min_deque.popleft()
                
                j += 1
            
            max_len = max(max_len,i - j + 1)
        

        return max_len

