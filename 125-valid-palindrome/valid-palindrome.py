class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # s = s.lstrip()
        # s = s.rstrip()
        # s = s.strip()
        # s = s.replace(" ","")
        s = re.sub(r'\s+',"",s)


        res = ""
        
        for ch in s:
            if ch.isalnum():
                res += ch
        
        l = 0
        r = len(res) - 1

        while l <= r:
            if res[l] == res[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        
        return True