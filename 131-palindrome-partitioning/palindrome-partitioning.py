class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        def isPalindrome(t):
            n = len(t)
            i = 0
            j = n - 1

            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        def backtracking(index,temp):
            if index == n:
                result.append(temp.copy())
                return
            
            for j in range(index,n):
                if isPalindrome(s[index:j + 1]):
                    temp.append(s[index:j + 1])
                    backtracking(j + 1, temp)
                    temp.pop()
            
        
        backtracking(0, [])
        return result






