# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs_helper_recursive(root,arr):
            if root:
                arr.append(root.val)
                dfs_helper_recursive(root.left, arr)
                dfs_helper_recursive(root.right, arr)
        
        arr = []
        dfs_helper_recursive(root,arr)
        if arr[0]*len(arr) == sum(arr):
            return True 
        else:
            return False

        