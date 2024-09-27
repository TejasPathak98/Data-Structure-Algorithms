class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        
        count = Counter(s)
        my_set = set()

        for ch in order:
            if ch in s:
                freq = count.get(ch)
                ans = ans + ch * freq
                my_set.add(ch)
        
        for ch in s:
            if ch not in my_set:
                ans = ans + ch
        
        return ans



        