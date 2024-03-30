# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        if not root.left and not root.right:
            return True 
        
        min_x = float("-inf")
        max_x = float("inf")
        
        def helper(root,mi,ma):
            if root == None:
                return True
            
            if root.val >= ma or root.val <= mi:
                return False
            else:
                return helper(root.left,mi,root.val) and helper(root.right,root.val,ma) 
        
        return helper(root,min_x,max_x)
        


         


        