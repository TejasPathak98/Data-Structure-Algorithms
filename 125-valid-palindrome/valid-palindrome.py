class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for ch in s:
            if ch.isalnum():
                st += ch.lower()
        
        return st == st[::-1]