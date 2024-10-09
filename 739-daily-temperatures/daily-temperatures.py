class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        stack = []
        stack.append((0,temperatures[0]))

        for i in range(1,n):
            if stack:
                while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                    index,_ = stack.pop()
                    ans[index] = i - index
            stack.append((i,temperatures[i]))

        return ans 

            
        