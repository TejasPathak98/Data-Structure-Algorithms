class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        @lru_cache
        def DP_helper(word):
            n = len(word)

            for i in range(n):
                x = word[:i + 1]
                y = word[i + 1:]

                if x in Wordset:
                    if y in Wordset or DP_helper(y):
                        return True

                
            return False

        Wordset = set(words)
        result = []

        for word in Wordset:
            Wordset.discard(word)

            if DP_helper(word):
                result.append(word)
            
            Wordset.add(word)

        
        return result

