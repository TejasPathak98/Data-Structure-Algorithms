class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque() #monotonically decreasing
        min_deque = deque() #monotonically increasing
        i = 0
        max_len = 0

        for j in range(len(nums)):

            while max_deque and nums[j] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[j])

            while min_deque and nums[j] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[j])


            while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:

                if max_deque and max_deque[0] == nums[i]:
                    max_deque.popleft()
                
                if min_deque and min_deque[0] == nums[i]:
                    min_deque.popleft()

                i += 1

            max_len = max(max_len,j - i + 1)
        

        return max_len
                




