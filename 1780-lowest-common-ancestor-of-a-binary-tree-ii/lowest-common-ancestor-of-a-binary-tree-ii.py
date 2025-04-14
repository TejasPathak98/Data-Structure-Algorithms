# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def Existence(node,X):
            if node.val == X.val:
                return True

            left = right = False
            
            if node.left:
                left = Existence(node.left,X)
            if node.right:
                right = Existence(node.right,X)
            
            return left or right

        if Existence(root, p) == False or Existence(root, q) == False:
            return None
        else:
            return self.LCA(root,p,q)


    def LCA(self,root,p,q):
        if root is None:
            return root

        if root == p or root == q:
            return root
        
        l = self.LCA(root.left, p, q)
        r = self.LCA(root.right, p, q)

        if l and r:
            return root
        
        return l if l else r