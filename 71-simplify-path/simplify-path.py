class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        l = [x for x in l if x != '.' and x != '']


        stack = []
        i = 0

        while i < len(l):
            if l[i] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(l[i])
            i += 1
        
        return '/' + '/'.join(stack)

        