class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        ans = []

        for word in words:
            l_word = word.lower()

            for row in rows:
                if all(ch in row for ch in l_word):
                    ans.append(word) 
                    break 
        
        return ans


