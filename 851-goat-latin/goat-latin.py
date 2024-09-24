class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = []
        words = sentence.split()
        vowels = ['a','e','i','o','u','E','A','I','U','O']
        new_words = []

        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i] = words[i] + "ma" + "a"*(i+1)
            else:
                x = words[i][0]
                words[i] = words[i][1:] + x + "ma" + "a"*(i+1)
        
        return ' '.join(words)





        
        
        
        