# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        

        def dfs(node):
            if not node:
                return True,0
            
            balanced_left,l = dfs(node.left)
            balanced_right,r = dfs(node.right)

            if not balanced_left or not balanced_right or (balanced_left and balanced_right and abs(l - r) >  1):
                return False,max(l,r)

            
            return (True,1 + max(l,r))

        
        return dfs(root)[0]

            