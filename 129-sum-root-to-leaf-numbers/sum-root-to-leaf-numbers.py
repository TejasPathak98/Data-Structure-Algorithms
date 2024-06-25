# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,current_sum):
            if not root:
                return 0
            current_sum = current_sum*10 + root.val 
            if root.left is None and root.right is None:
                return current_sum
            left_sum = dfs(root.left,current_sum)
            right_sum = dfs(root.right,current_sum)

            return left_sum + right_sum

        return dfs(root,0)        