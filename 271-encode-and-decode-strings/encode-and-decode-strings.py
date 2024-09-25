class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = []

        for st in strs:
            for c in st:
                result.append(str(ord(c)))
                result.append(';')
            result.append(' ')

        print(''.join(result))
    
        return ''.join(result)

        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        strings = s.split(' ')

        for st in strings:
            temp = []
            for ch in st.split(';'):
                if ch:
                    temp.append(chr(int(ch)))
            ans.append(''.join(temp))
        
        
        ans.pop()
        return ans
        


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))