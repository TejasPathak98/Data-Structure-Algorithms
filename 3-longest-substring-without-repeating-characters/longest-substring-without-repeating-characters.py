class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0 or n == 1:
            return n

        max_ans = 0
        i = 0
        j = 0
        
        dic = defaultdict(int)
        #dic[s[0]] = 0

        while j < n:
            if s[j] in dic and dic[s[j]] >= i:
                i = dic[s[j]] + 1
            dic[s[j]] = j
            print(f"{i} ; {j}")
            max_ans = max(max_ans,j - i + 1)
            print(max_ans)
            j += 1
            print(j)
            
        return max_ans


            


