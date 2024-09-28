class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = []

        i  = 0

        while i < n:
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                st.append(s[i])
            elif s[i] == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False
            elif s[i] == "]":
                if st and st[-1] == "[":
                    st.pop()
                else:
                    return False
            elif s[i] == "}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    return False
            i += 1
        
        return len(st) == 0
        