# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def helper(root):
            if root is None:
                return True,0
            
            left_balanced,left_height = helper(root.left)
            right_balanced,right_height = helper(root.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return balanced,1 + max(left_height,right_height)
        
        return helper(root)[0]

        