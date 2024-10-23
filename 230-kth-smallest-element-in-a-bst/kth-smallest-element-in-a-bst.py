# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []
        def Inorder(root):
            if not root:
                return
            
            Inorder(root.left)
            self.l.append(root.val)
            Inorder(root.right)
        
        Inorder(root)
        return self.l[k - 1]


        