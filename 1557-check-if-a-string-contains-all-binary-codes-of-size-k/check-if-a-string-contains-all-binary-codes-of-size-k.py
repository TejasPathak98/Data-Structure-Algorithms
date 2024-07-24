class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        i = 0
        j = k
        st = set()

        st.add(s[i:j])
        j += 1
        
        for i in range(1,len(s) - k + 1):
            st.add(s[i:j])
            j += 1 

       
        
        return len(st) == 2**k