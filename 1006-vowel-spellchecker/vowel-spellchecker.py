class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def unvowel(word):
            return ''.join("*" if ch  in 'aeiou' else ch for ch in word.lower())

        set_wordlist = set(wordlist)
        case_insensitive = {}
        vowel_insensitive = {}
        result = []

        for word in wordlist:
            if word.lower() not in case_insensitive:
                case_insensitive[word.lower()] = word
            if unvowel(word) not in vowel_insensitive:
                vowel_insensitive[unvowel(word)] = word
        

        for query in queries:
            if query in set_wordlist:
                result.append(query)
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            elif unvowel(query) in vowel_insensitive:
                result.append(vowel_insensitive[unvowel(query)])
            else:
                result.append("")
        
        return result

