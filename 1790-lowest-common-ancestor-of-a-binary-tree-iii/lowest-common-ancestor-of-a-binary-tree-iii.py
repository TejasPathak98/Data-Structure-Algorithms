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
        if p.parent == q:
            return q
        if q.parent == p:
            return p
        if p.parent == q.parent:
            return p.parent
        
        temp = p

        while temp.parent:
            temp = temp.parent
        
        root = temp

        def helper(root,p,q):
            if root is None or p == root or q == root:
                return root
            
            l = helper(root.left,p,q)
            r = helper(root.right,p,q)

            if l and r:
                return root
            
            return l if l else r
        
        return helper(root,p,q)


        