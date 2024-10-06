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
        
        
        
        def dfs(root,x):
            if root is None:
                return 0

            x = x*10 + root.val

            if root.left is None and root.right is None:
                return x

            l = dfs(root.left,x)
            r = dfs(root.right,x)

            return l + r
        
        return dfs(root,0)
        