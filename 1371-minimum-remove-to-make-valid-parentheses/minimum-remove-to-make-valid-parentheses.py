class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)

        i = 0
        while i < len(s_list):
            if s_list[i] == "(":
                stack.append(i)
            elif s_list[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s_list = s_list[:i] + s_list[i + 1:]
                    i -= 1
            i += 1

        while stack:
            pos = stack.pop()
            s_list = s_list[:pos] + s_list[pos + 1:]

        return "".join(s_list)   