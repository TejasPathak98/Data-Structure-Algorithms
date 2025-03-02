class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = []

        i = 0

        while i < len(temperatures):
            if not stack:
                stack.append(i)
            elif temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    pos = stack.pop()
                    answer[pos] = i - pos
                stack.append(i)
            else:
                stack.append(i)
            i += 1
        
        return answer

