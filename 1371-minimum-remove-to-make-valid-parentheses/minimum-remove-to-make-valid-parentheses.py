class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)
        print(s_list)

        i = 0
        j = 0

        while i < len(s_list):
            if s_list[i] == "(":
                stack.append((s_list[i],i))
            elif s_list[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s_list = s_list[:i] + s_list[i + 1:]
                    i -= 1
            i += 1

        while stack:
            _, pos = stack.pop()
            s_list = s_list[:pos] + s_list[pos + 1:]

        print(s_list)
        return "".join(s_list)   