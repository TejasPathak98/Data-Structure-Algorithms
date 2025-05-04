# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs_existence_check(node,p):
            if not node:
                return False
            
            if node is p:
                return True
            
            return dfs_existence_check(node.left, p) or dfs_existence_check(node.right, p)

        if not dfs_existence_check(root, p) or not dfs_existence_check(root,q):
            return None
        

        def LCA(root,p,q):
            if not root:
                return None
            
            if root is p or root is q:
                return root

            l = LCA(root.left,p,q)
            r = LCA(root.right,p,q)

            if l and r:
                return root
            
            return l if l else r
        
        return LCA(root,p,q)