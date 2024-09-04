# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        def dfs(root,ans):
            if root.left == None and root.right == None:
                ans += 1
                return ans
            elif root.left == None:
                return dfs(root.right,ans + 1)
            elif root.right == None:
                return dfs(root.left,ans + 1)
            return min(dfs(root.left,ans + 1),dfs(root.right,ans + 1))
        
        return dfs(root,0)

         
        