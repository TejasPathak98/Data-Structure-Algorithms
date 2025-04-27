class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        final_str = ""

        for s in strs:
            temp = ""
            for ch in s:
                temp += str(ord(ch)) + "#"
            final_str += temp + "*"
        return final_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        final_list = []
        string_split = s.split("*")
        string_split = string_split[:-1]

        for st in string_split:
            s_split = st.split("#")
            s_split = s_split[:-1]
            temp = ""
            for ch in s_split:
                temp += chr(int(ch))
            final_list.append(temp)
        
        return final_list
            


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))