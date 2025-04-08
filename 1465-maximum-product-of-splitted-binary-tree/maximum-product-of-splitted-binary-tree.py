# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        sums = []

        def dfs(root):
            if not root:
                return 0
            Sum = dfs(root.left) + dfs(root.right) + root.val
            sums.append(Sum)
            return Sum
        
        max_prod = float('-inf')
        total_sum = dfs(root)
        for s in sums:
            prod = s * (total_sum - s)
            max_prod = max(max_prod,prod)
        
        return max_prod % (10 ** 9  + 7)