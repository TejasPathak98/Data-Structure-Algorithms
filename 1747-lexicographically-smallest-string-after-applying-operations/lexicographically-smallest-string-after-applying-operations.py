class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def op1(s):
            res = []

            for i,c in enumerate(s):
                if i % 2 == 1:
                    res.append(str((int(c) + a) % 10))
                else:
                    res.append(c)
            
            return ''.join(res)

        def op2(s):
            return s[-b:] + s[:-b]

        stack = []
        stack.append(s)
        seen = set()

        while stack:
            x = stack.pop()
            seen.add(x)

            r1 = op1(x)
            if r1 not in seen:
                stack.append(r1)

            r2 = op2(x)
            if r2 not in seen:
                stack.append(r2)

        return min(seen)

        
                