# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        first = second = prev = None

        def dfs_InOrder(node):
            nonlocal first,second,prev
            if not node:
                return
            
            dfs_InOrder(node.left)

            if prev and prev.val > node.val:
                if first == None:
                    first = prev
                
                second = node
            
            prev = node

            dfs_InOrder(node.right)

        dfs_InOrder(root)

        first.val , second.val = second.val , first.val