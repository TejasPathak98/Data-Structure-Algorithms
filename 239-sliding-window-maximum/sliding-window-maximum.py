class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_heap = []
        # ans = []

        # for i in range(k):
        #     max_heap.append(-nums[i])
        
        # heapify(max_heap)
        # r = k

        # ans.append(-max_heap[0])
        # l = 0

        # while r < len(nums):
        #     x = nums[l]
        #     to_add = []

        #     while max_heap:
        #         val = -heapq.heappop(max_heap)
        #         if val != x:
        #             to_add.append(val)
        #         else:
        #             break
            
        #     for y in to_add:
        #         heapq.heappush(max_heap, -y)
            
        #     heapq.heappush(max_heap,-nums[r])
            

        #     ans.append(-max_heap[0])
        #     l += 1
        #     r += 1
        
        # return ans

        #This is lazy deletion method(TLE)


        ans =  []
        ans.append(max(nums[:k]))
        
        stack = deque()

        for i in range(k):
            if not stack:
                stack.append((nums[i],i))
            else:
                if nums[i] > stack[-1][0]:
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






















