class Solution:
    def simplifyPath(self, path: str) -> str:
        var = path.split("/")
        var = [x for x in var if x != '.' and x != '']
        stack = []
        i = 0

        while i < len(var):
            if var[i] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(var[i])
            i += 1

        return "/" + "/".join(stack)

        