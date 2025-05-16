class Solution:
    def simplifyPath(self, path: str) -> str:
        var = path.split('/')
        var = [x for x in var if x not in (".","")]
        var = var[::-1]
        stack = []

        while var:
            st = var.pop()

            if st == "..":
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(st)


        return "/" + "/".join(stack)
