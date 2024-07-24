class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s) 
        n2 = len(p)
        arr = []

        i = 0 
        j = n2

        char_count = defaultdict(int)
        ptr = defaultdict(int)
        for ch in p:
            char_count[ch] += 1

        for ch in s[i:j]:
            ptr[ch] += 1
        
        if char_count == ptr:
            arr.append(0)

        for i in range(1,n1 - n2 + 1):
            ptr[s[i - 1]] -= 1
            if ptr[s[i - 1]] == 0:
                del ptr[s[i - 1]]
                
            ptr[s[j]] += 1
            j += 1

            print(ptr)

            if char_count == ptr:
                arr.append(i) 
                
        return arr
        
        
        
        



