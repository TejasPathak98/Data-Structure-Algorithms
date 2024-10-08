"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        self.first = self.last = None

        self.dfs_linker(root)

        self.last.right = self.first
        self.first.left = self.last

        return self.first
    
    def dfs_linker(self,node):

        if node is None:
            return
        
        self.dfs_linker(node.left)

        if not self.last:
            self.first = node
        else:
            node.left = self.last
            self.last.right = node
        
        self.last = node

        self.dfs_linker(node.right)
    


        