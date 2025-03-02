class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(temp_str,left_count,right_count):
            if left_count + right_count == 2 * n:
                answer.append(temp_str)
                return
            if left_count < n:
                backtrack(temp_str + "(", left_count + 1, right_count)
            if right_count < left_count:
                backtrack(temp_str + ")", left_count, right_count + 1)
        
        backtrack("", 0, 0)
        return answer
