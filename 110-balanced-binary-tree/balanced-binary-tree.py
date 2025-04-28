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
                return 0,True
            
            left_height,isLeftBST = dfs(node.left)
            right_height,isRightBST = dfs(node.right)

            if isLeftBST == False or isRightBST == False:
                return 1 + max(left_height,right_height),False

            if abs(left_height - right_height) > 1:
                return 1 + max(left_height,right_height),False
            
            return 1 + max(left_height,right_height),True
    

        return dfs(root)[1]


        
