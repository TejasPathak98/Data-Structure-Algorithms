class Solution:
    def simplifyPath(self, path: str) -> str:
        var = path.split('/')

        print(var)

        var = [x for x in var if x not in (".","")]

        print(var)

        var = var[::-1]

        print(var)

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
