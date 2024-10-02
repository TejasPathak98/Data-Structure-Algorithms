class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapy = [-2] * 32
        mapy[0] = -1

        mask = 0
        max_len = 0

        for i,char in enumerate(s):
            
            if char == 'a':
                mask ^= 1
            if char == 'e':
                mask ^= 2
            if char == 'i':
                mask ^= 4
            if char == 'o':
                mask ^= 8
            if char == 'u':
                mask ^= 16

            if mapy[mask] == -2:
                mapy[mask] = i 
            else:
                prev = mapy[mask]
                max_len = max(max_len,i - prev)

        
        return max_len
            
