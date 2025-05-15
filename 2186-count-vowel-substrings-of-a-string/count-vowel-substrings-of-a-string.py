class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a','e','i','o','u'}
        start = 0
        vowel_idx = {}
        result = 0

        for idx,ch in enumerate(word):
            if ch in vowels:
                if not vowel_idx:
                    start = idx
                
                vowel_idx[ch] = idx

                if len(vowel_idx) == 5:
                    min_idx = min(vowel_idx.values())

                    result += min_idx - start + 1
            else:
                vowel_idx = {}

        
        return result

                    
