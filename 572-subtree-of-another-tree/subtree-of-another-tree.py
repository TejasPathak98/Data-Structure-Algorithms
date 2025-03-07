# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root,subRoot)

    def dfs(self,root,subRoot):
        if not root:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        return self.dfs(root.left,subRoot) or self.dfs(root.right,subRoot)
    
    def isSameTree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
 
