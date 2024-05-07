class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = deque()
        ans = [0] * n 

        for log in logs:
            id,action,timestamp = log.split(":")
            id,timestamp = int(id) , int(timestamp) 

            if action == 'start':
                stack.append((id,timestamp))
            else:
                id, start_time = stack.pop() 
                elapsed_time = timestamp - start_time + 1
                ans[id] += elapsed_time

                if stack:
                    ans[stack[-1][0]] -= elapsed_time 
        
        return ans

        