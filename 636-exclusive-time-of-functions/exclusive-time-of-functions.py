class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n

        stack = []

        for log in logs:
            components = log.split(":")
            time = int(components[2])
            ID = int(components[0])

            if not stack:
                stack.append([ID,time])
            else:
                if components[1] == "start":
                    stack.append([ID,time])
                else:
                    ID,start_time = stack.pop()
                    ans[ID] += (time - start_time + 1)

                    if stack:
                        ans[stack[-1][0]] -= (time - start_time + 1)
        
        return ans
            

