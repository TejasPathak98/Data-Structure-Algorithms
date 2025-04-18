class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_len = 0
        j = 0
        i = 0

        if k == 0:
            while j < len(nums):
                if nums[j] == 1:
                    max_len = max(max_len,j - i + 1)
                    j += 1
                else:
                    i = j + 1
                    j += 1
            
            return max_len

        queue = deque()

        while j < len(nums):
            if nums[j] == 1:
                max_len = max(max_len,j - i + 1)
                j += 1
            else:
                if k > 0:
                    max_len = max(max_len,j - i + 1)
                    queue.append(j)
                    j += 1
                    k -= 1
                else:
                    if not queue:
                        i = j + 1
                        j += 1
                    else:
                        pos = queue.popleft()
                        queue.append(j)
                        i = pos + 1
                        max_len = max(max_len,j - i + 1)
                        j += 1

        
        return max_len


        