class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        s1 = strs[0]
        s2 = strs[-1]

        for i in range(min(len(s1),len(s2))):
            if s1[i] != s2[i]:
                return ans
            ans += s1[i]
        
        return ans
        