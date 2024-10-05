class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        
        if len(word) == 1:
            if abbr == '1' or abbr == word:
                return True
            else:
                return False

        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            elif abbr[j].isdigit():
                if int(abbr[j]) == 0:
                    return False
                x = 0
                while  j < len(abbr) and abbr[j].isdigit():
                    x = x*10 + int(abbr[j])
                    j += 1
                i = i + x
                if i > len(word):
                    return False
            elif word[i] != abbr[j] and not word[i].isdigit() and not abbr[j].isdigit():
                return False
        
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False
            


        