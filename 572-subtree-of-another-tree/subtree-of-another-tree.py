# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if not p and q:
                return False
            if not q and p:
                return False
            if not q and not p:
                return True
            if p.val != q.val:
                return False
            return helper(p.left,q.left) and helper(p.right,q.right)

        def dfs(node):
            if not node:
                return False
            
            if helper(node,subRoot) == True:
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)