class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        start = 0
        end = len(s) - 1
        s = s.lower()

        while start <= end:
            while start <= end and not s[start].isalnum():
                start += 1
            while start <= end and not s[end].isalnum():
                end -= 1
            
            if start <= end and s[start] == s[end]:
                start += 1
                end -= 1
            else:
                break
        
        if start < end:
            return False
        else:
            return True
            


        