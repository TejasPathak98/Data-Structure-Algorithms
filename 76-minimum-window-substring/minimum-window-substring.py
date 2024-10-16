class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        if m == n:
            if Counter(s) == Counter(t):
                return s
            else:
                return ""

        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        dict_s = defaultdict(int)
        l = 0 
        r = 0
        ans = float("inf"),l,r
        formed = 0
        required = len(dict_t)

        while r < len(s):
            dict_s[s[r]] += 1
            if dict_s[s[r]] == dict_t[s[r]]:
                formed += 1
            
            while l < len(s) and formed == required:
                if ans[0] > r - l + 1:
                    ans = r - l + 1,l,r
                
                dict_s[s[l]] -= 1
                if dict_s[s[l]] < dict_t[s[l]]:
                    formed -= 1
                l += 1
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

        