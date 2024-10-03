# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        mi = float('-inf')
        ma = float('inf')

        def helper(root,mi,ma):
            if root is None:
                return True
            
            if root.val <= mi or root.val >= ma:
                return False
            
            return helper(root.left,mi,root.val) and helper(root.right,root.val,ma)

        return helper(root,mi,ma)