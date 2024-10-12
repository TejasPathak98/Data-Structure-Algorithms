class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        st = path.split('/')
        st = [x for x in st if x != '.' and x != '']
        stt = ""
        
        i = 0
        while i < len(st):
            if st[i] == "..":
                if i == 0:
                    st.pop(i)
                    i -= 1
                else:
                    st.pop(i - 1)
                    i -= 1
                    st.pop(i)
                    i -= 1
            i += 1

        #for t in st:


        return "/" + "/".join(st)