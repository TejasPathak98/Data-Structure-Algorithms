# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        Min = float("-inf")
        Max = float("inf")

        return self.dfs(root,Min,Max)
    
    def dfs(self,root,Min,Max):
        if root is None:
            return True
        
        if root.val >= Max or root.val <= Min:
            return False
        
        return self.dfs(root.left,Min,root.val) and self.dfs(root.right,root.val,Max)
    