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
        
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            l = max(dfs(node.left) , 0) #clamp all the negative contribution from the child
            r = max(dfs(node.right) , 0)

            max_sum = max(max_sum,node.val + l + r)

            
            return max(l,r) + node.val

        
        dfs(root)
        return max_sum
