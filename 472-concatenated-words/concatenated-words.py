from functools import cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        result = []

        @cache(lru_cache)
        def helper(word):
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordSet:
                    if suffix in wordSet or helper(suffix):
                        return True
                
            return False
                

        for word in words:
            wordSet.discard(word)
            if helper(word):
                result.append(word)
            wordSet.add(word)

        return result