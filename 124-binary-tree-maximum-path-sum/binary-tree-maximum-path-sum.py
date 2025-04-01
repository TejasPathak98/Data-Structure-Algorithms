# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            lsum = dfs(node.left)
            rsum = dfs(node.right)

            self.max_sum = max(self.max_sum,lsum + rsum + node.val,node.val,lsum + node.val,rsum + node.val)

            return max(lsum + node.val,rsum + node.val,node.val)

        dfs(root)
        return self.max_sum

            




