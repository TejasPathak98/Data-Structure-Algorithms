# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        #we have to store the sums of the tree in post order dfs manner and then iterate over the array

        sums = []

        def dfs(node):
            if not node:
                return 0
            Sum = dfs(node.left) + dfs(node.right) + node.val
            sums.append(Sum)
            return Sum

        max_product = float("-inf")
        total_sum = dfs(root)

        for s in sums:
            left_product = s
            right_product = total_sum - left_product
            max_product = max(max_product,left_product* right_product)

        return max_product % (10**9 + 7)
