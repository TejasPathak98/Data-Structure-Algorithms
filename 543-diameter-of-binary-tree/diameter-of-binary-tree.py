# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.diameter = 0
        
        def depth(root):
            if not root:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)

            self.diameter = max(self.diameter,l + r)

            return max(l,r) + 1
        
        depth(root)
        return self.diameter

        