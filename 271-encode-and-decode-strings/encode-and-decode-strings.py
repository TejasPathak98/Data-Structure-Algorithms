class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        temp = ""

        for st in strs:
            for c in st:
                temp += (str(ord(c)) + ";")
            temp += " "
                    
        return temp

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        stt = s.split(" ")
        res = []

        for st in stt:
            temp = []
            t = st.split(";")
            for x in t:
                if x:
                    temp.append(chr(int(x)))
            res.append("".join(temp))
        
        res.pop()
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))