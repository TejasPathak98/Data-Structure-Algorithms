class Solution:
    def expand(self, s: str) -> List[str]:
        i = 0
        res = []
        options = []

        while i < len(s):
            if s[i] == "{":
                temp = []
                while s[i] != "}":
                    if s[i].isalpha():
                        temp.append(s[i])
                    i += 1
                temp.sort()
                options.append(temp)
            else:
                if s[i].isalpha():
                    options.append([s[i]])
                i += 1
        print(options)

        def backtracking(index,tempstr):
            if len(tempstr) == len(options):
                res.append(tempstr)
                return
            for st in options[index]:
                prev = tempstr
                tempstr += st
                backtracking(index + 1, tempstr)
                tempstr = prev
        
        backtracking(0,"")
        return res