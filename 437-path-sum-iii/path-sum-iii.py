# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        def dfs(root,current_sum):
            if root is None:
                return 0
            
            current_sum += root.val
            path_count = prefix_sums[current_sum - targetSum]
            prefix_sums[current_sum] += 1

            path_count += dfs(root.left,current_sum)
            path_count += dfs(root.right,current_sum)

            prefix_sums[current_sum] -= 1

            return path_count

        return dfs(root,0)
            