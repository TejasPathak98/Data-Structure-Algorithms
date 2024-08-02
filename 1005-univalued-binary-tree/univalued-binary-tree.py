# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs_helper_iterative(root,arr):
            if root is None:
                return
            
            stack = []
            stack.append(root)

            while stack:
                node = stack.pop()
                arr.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
            return
        
        arr = []
        dfs_helper_iterative(root,arr)
        if arr[0]*len(arr) == sum(arr):
            return True 
        else:
            return False

        