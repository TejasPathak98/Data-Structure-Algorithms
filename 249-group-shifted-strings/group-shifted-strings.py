class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        n = len(strings)
        if n == 1:
            return [strings[0]]
        
        dic = defaultdict(list)
        ans = []
        t = []

        for st in strings:
            if len(st) == 1:
                t.append(st)
            else:
                i = 0
                temp = []
                while i <= len(st) - 2:
                    diff = (ord(st[i + 1]) - ord(st[i]) + 26) % 26
                    temp.append(diff)
                    i += 1
                dic[tuple(temp)].append(st)
        
        for key,v in dic.items():
            ans.append(v)
        
        if t:
            ans.append(t)
        
        return ans
        
        


        