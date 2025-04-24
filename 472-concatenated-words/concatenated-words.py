class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        @lru_cache
        def DP_helper(word):
            n = len(word)

            for i in range(n):
                x = word[:i + 1]
                y = word[i + 1:]

                if x in words:
                    if y in words or DP_helper(y):
                        return True
            return False

        words = set(words)
        result = []

        for word in words:
            words.discard(word)

            if DP_helper(word):
                result.append(word)
            
            words.add(word)

        
        return result

