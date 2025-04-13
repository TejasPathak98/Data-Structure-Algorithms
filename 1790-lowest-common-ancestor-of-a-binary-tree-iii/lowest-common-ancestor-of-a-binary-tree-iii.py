"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def dfs_get_root(node):            
            if node.parent == None:
                return node
            
            return dfs_get_root(node.parent)

        root = dfs_get_root(p)

        def lca(root,p,q):
            if not root:
                return root
            
            if root == p or root == q:
                return root
            
            l = lca(root.left,p,q)
            r = lca(root.right,p,q)

            if l and r:
                return root
            
            return l if l else r

        
        return lca(root,p,q)


        