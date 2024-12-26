class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = float('-inf')

        for val in preorder:
            if val < lower_bound:
                return False
            
            while stack and val > stack[-1]:
                lower_bound = stack.pop()
            
            stack.append(val)
        
        return True
        