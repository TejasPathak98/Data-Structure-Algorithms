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
        self.root = None
        
        def get_root(node):
            if node.parent is None:
                return node
            
            return get_root(node.parent)

        self.root = get_root(p)

        
        def LCA(root,p,q):
            if not root:
                return root
            
            if root == p or root  == q:
                return root
            
            l = LCA(root.left,p,q)
            r = LCA(root.right,p,q)

            if l and r:
                return root
            
            return l if l else r

        return LCA(self.root,p,q)


