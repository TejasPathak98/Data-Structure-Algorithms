class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string_to_send = ""
        for string in strs:
            temp_string =""
            for ch in string:
                c = str(ord(ch))
                temp_string += c + "*"
            string_to_send += temp_string + "-"        
        return string_to_send

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        strings = s.split("-")[:-1]
        for string in strings:
            temp_strings = string.split("*")[:-1]
            ts = ""
            for st in temp_strings:
                ch = chr(int(st))
                ts += ch
            ans.append(ts)
        
        return ans



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))