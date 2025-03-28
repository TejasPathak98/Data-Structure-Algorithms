class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans = []
        stack = []

        for i,x in enumerate(s + "I"):
            if x == "D":
                stack.append(i + 1)
            else:
                ans.append(i + 1)
                while stack:
                    ans.append(stack.pop())
        
        return ans
        