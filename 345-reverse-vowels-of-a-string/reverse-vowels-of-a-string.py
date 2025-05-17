class Solution:
    def reverseVowels(self, s: str) -> str:
        pos = set()
        chs = []
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        for i in range(len(s)):
            if s[i] in vowels:
                pos.add(i)
                chs.append(s[i])

        
        i = len(chs) - 1

        print(chs)
        
        new_s = ""

        for j in range(len(s)):
            if j not in pos:
                new_s += s[j]
            else:
                new_s += chs[i]
                i -= 1

        return new_s


        

