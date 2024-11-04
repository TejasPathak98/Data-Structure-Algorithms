class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        stack = []
        curr_string = ""

        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                num_stack.append(num)
            elif s[i] == "[":
                stack.append(curr_string)
                curr_string = ""
                i += 1
            elif s[i].isalpha():
                curr_string += s[i]
                i += 1
            else:
                x = num_stack.pop() if num_stack else 1
                curr_string = stack.pop() + curr_string*x
                i += 1


        return curr_string






        