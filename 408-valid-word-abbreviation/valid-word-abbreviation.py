class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)

        if len(abbr) > len(word):
            return False

        i = 0 
        j = 0
        while i < n and j < m:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            elif abbr[j].isdigit():
                if int(abbr[j]) == 0:
                    return False
                s = j
                if j == m - 1:
                    number = int(abbr[j])
                    if number == len(word[i:]):
                        return True
                    else:
                        return False
                else:
                    while j < m and abbr[j].isdigit():
                        j += 1
                    number = int(abbr[s:j])
                i += number
            else:
                return False
        
        if i == n and j == m:
            return True
        else:
            return False


        