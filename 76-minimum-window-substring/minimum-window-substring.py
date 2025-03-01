class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_dict = Counter(t)
        s_dict = defaultdict(int)

        l = 0 
        r = 0
        ans = float('inf'),l,r
        required = len(t_dict)
        formed = 0

        while r < len(s):
            s_dict[s[r]] += 1
            if s_dict[s[r]] == t_dict[s[r]]:
                formed += 1
            
            while l < len(s) and formed == required:
                if ans[0] > r - l + 1:
                    ans = r - l + 1,l,r
                
                s_dict[s[l]] -= 1
                if s_dict[s[l]] < t_dict[s[l]]:
                    formed -= 1

                l += 1
            r += 1
        

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


