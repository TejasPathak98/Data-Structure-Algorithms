# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.count = 0
        def dfs(root):
            if root.left is not None:
                left_val = dfs(root.left)
            else:
                left_val = root.val
            

            if root.right is not None:
                right_val = dfs(root.right)
            else:
                right_val = root.val
            
            if left_val == right_val == root.val:
                self.count += 1
                return root.val
            else:
                return None


        dfs(root)
        return self.count