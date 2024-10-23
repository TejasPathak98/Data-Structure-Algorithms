class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i].isalnum():
                st += s[i].lower()
        
        return st == st[::-1]