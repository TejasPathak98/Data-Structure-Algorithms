# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        self.total_sum = 0
        
        def dfs(root):
            if not root:
                return
            
            if low <= root.val <= high:
                self.total_sum += root.val
                dfs(root.left)
                dfs(root.right)
            elif root.val > high:
                dfs(root.left)
            else:
                dfs(root.right)
            
        
        dfs(root)
        return self.total_sum


        