class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        ans = []
        ans.append(max(nums[:k]))

        for i in range(k):
            if not stack:
                stack.append((nums[i],i))
            else:
                if nums[i] >= stack[-1][0]:
                    stack.append((nums[i],i))
                else:
                    while nums[i] > stack[0][0]:
                        stack.popleft()
                    stack.appendleft((nums[i],i))

        
        for r in range(k,len(nums)):
            if nums[r] >= stack[-1][0]:
                stack.append((nums[r],r))
                ans.append(stack[-1][0])
            else:
                while nums[r] > stack[0][0]:
                    stack.popleft()
                stack.appendleft((nums[r],r))

                while stack[-1][1] <= r - k:
                    stack.pop()
                
                ans.append(stack[-1][0])
        

        return ans