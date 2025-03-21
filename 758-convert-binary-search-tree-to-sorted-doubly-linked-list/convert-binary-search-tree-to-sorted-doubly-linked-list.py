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
            return
        
        def dfs_linker(root):
            if not root:
                return
            
            dfs_linker(root.left)

            if not self.first:
                self.first = root
            else:
                self.last.right = root
                root.left = self.last

            self.last = root

            dfs_linker(root.right)



        self.first = None
        self.last = None

        dfs_linker(root)

        self.first.left = self.last
        self.last.right = self.first

        return self.first
    
    