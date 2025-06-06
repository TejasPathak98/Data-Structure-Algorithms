class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A
        stack = [0]
        result = [0] * len(A)

        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i - j) * A[i]
            stack.append(i)
        
        return sum(result) % (10 ** 9 + 7)