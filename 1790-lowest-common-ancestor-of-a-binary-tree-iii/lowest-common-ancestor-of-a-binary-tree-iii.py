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
            if root == None or root == p or root == q:
                return root
            
            left = helper(root.left,p,q)
            right = helper(root.right,p,q)

            if left and right:
                return root
            
            return left if left else right

        return helper(root,p,q)

            

        

        