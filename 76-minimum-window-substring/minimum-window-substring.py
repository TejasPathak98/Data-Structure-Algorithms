class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == len(s):
            if Counter(t) == Counter(s):
                return s
            else:
                return ""

        
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        l = 0
        r = 0
        result = [float('inf'),l,r]
        dict_s = defaultdict(int)

        while r < len(s):
            dict_s[s[r]] += 1
            if dict_s[s[r]] == dict_t[s[r]]:
                formed += 1
            
            while l <= r and formed == required:
                if (r - l + 1) < result[0]:
                    result = [r - l + 1,l,r]
                
                dict_s[s[l]] -= 1
                if s[l] in dict_t and dict_s[s[l]] < dict_t[s[l]]:
                    formed -= 1

                l += 1

            r += 1

        return s[result[1]:result[2] + 1] if result[0] != float('inf') else ""
        

            








