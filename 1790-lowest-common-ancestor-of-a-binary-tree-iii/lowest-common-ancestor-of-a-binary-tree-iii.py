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
        parent_map = {}

        node = p

        while node:
            parent_map[node] = node.parent
            node = node.parent

        while q:
            if q in parent_map:
                return q
            q = q.parent
        
        return None
        
