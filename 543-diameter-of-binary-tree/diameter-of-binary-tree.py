# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        self.diameter = 0

        def helper(node):
            if not node:
                return 0
            
            l = helper(node.left)
            r = helper(node.right)

            self.diameter = max(self.diameter,l + r)

            return max(l,r) + 1
        
        helper(root)
        return self.diameter
        