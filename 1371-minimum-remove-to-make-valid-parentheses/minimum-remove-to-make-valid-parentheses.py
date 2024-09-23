class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)

        st = []
        i = 0

        while i < len(s):
            x = ord(s[i]) - ord('a')
            if 0 <= x < 26:
                i += 1
                continue
            elif s[i] == "(":
                st.append((s[i],i))
            elif s[i] == ")":
                if st:
                    st.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                    
            i +=1

        while st:
            _,j = st.pop()
            s = s[:j] + s[j + 1:]
            
        return s


        