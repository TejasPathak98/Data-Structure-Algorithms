class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def helper(start,temp):
            if start == len(s):
                ans.append(temp[:])
                return
            
            for end in range(start + 1,len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    helper(end,temp + [s[start:end]])
        
        helper(0,[])
        return ans