class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        l = 0
        r = k - 1

        vowel_count = 0
        max_count = 0

        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1

        max_count = max(max_count,vowel_count)

        for r in range(k,len(s)):
            if s[r] in vowels:
                vowel_count += 1
               
            if s[l] in vowels:
                vowel_count -= 1
            l += 1 
            
            max_count = max(max_count,vowel_count)

        return max_count

