# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        final_sum = 0
        
        def helper(root,curr_sum):
            nonlocal final_sum
            if root.left is None and root.right is None:
                final_sum += curr_sum*10 + root.val
                return

            curr_sum = curr_sum*10 + root.val

            if root.left:
                helper(root.left,curr_sum)
            if root.right:
                helper(root.right,curr_sum)
        
        helper(root,0)
        return final_sum
        




        