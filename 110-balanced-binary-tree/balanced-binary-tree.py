# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)

    def dfs(self,root):
        if not root:
            return True
        
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        
        return self.dfs(root.left) and self.dfs(root.right)
    
    def depth(self,root):
        if root is None:
            return 0
        
        return 1 + max(self.depth(root.left),self.depth(root.right))