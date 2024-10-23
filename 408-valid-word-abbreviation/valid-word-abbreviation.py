class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if abbr[j].isnumeric():
                    if int(abbr[j]) == 0:
                        return False
                    val = 0
                    while j < len(abbr) and abbr[j].isnumeric():
                        val = val*10 + int(abbr[j])
                        j += 1
                    i = i + val
                else:
                    return False
        
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False
                    
        