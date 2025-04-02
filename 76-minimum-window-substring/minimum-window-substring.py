class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dict_t = Counter(t)
        requried = len(dict_t) # how many unique characters do I need to match ?
        formed =0 # how many unique characters have I matched ? Do not compare the full map
        l = 0
        r = 0
        ans = float("inf"),r,l
        s_dict = defaultdict(int)

        while r < len(s):
            s_dict[s[r]] += 1

            if s_dict[s[r]] == dict_t[s[r]]:# we match one unique char count
                formed += 1
            
            while l < len(s) and formed == requried:
                if ans[0] > r - l + 1:
                    ans = r-l+1,r,l

                s_dict[s[l]] -= 1

                if s_dict[s[l]] < dict_t[s[l]]:
                    formed -= 1
                
                l += 1

            r += 1

        if ans[0] == float("inf"):
            print("Br")
            return ""
        else:
            return s[ans[2]:ans[1] + 1]
