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
        
        root = None

        def reverse_traversal(node):
            nonlocal root
            if not node:
                return
            
            if node.parent is None:
                root = node
            
            reverse_traversal(node.parent)
        
        reverse_traversal(p)

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

            
