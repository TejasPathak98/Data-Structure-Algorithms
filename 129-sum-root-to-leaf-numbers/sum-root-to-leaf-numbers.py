# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        arr = []
        
        def dfs(root,x):
            nonlocal arr

            if root is None:
                return

            
            
            if root.left is None and root.right is None:
                x = x*10 + root.val
                arr.append(x)
                return
            
            x = x*10 + root.val

            dfs(root.left,x)
            dfs(root.right,x)
        
        dfs(root,0)
        print(arr)
        return sum(arr)

        