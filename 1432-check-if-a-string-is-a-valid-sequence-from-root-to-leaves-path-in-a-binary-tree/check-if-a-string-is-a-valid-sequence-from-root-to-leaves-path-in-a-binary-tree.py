# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:

        def dfs(root,index):

            if root is None or index >= len(arr):
                return False 
            
            if root.val != arr[index]:
                return False  
            
            if index == len(arr) - 1:
                return root.left is None and root.right is None
            
            return dfs(root.left,index + 1) or dfs(root.right,index + 1)
        
        return dfs(root,0)
        