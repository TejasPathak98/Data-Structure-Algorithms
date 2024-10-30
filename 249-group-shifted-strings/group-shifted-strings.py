class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        ans = []

        for s in strings:
            l = len(s)
            if l == 1:
                temp = [-1]
                my_dict[tuple(temp)].append(s)
            else:
                temp = []
                for i in range(1,len(s)):
                    temp.append( (ord(s[i]) - ord(s[i - 1]) + 26 ) % 26)
                my_dict[tuple(temp)].append(s)
        
        for k,val in my_dict.items():
            ans.append(val)
        
        return ans

        