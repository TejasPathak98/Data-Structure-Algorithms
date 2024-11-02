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
            return None
        
        self.first = None
        self.last = None

        self.dfs_linker(root)

        self.first.left = self.last
        self.last.right = self.first

        return self.first

    def dfs_linker(self,root):
        if not root:
            return
        
        self.dfs_linker(root.left)
        
        if not self.last:
            self.first = root
        else:
            self.last.right = root
            root.left = self.last
        
        self.last = root


        self.dfs_linker(root.right)