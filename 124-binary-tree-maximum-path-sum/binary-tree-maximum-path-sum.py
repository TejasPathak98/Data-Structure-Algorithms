# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:        
        self.helper(root)
        return self.max_sum
        
    def helper(self,root):
        if root is None:
            return 0
        
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)

        self.max_sum = max(self.max_sum,root.val + left_sum + right_sum,root.val,root.val + left_sum,root.val + right_sum)

        return max(root.val,root.val + left_sum,root.val + right_sum)



        
