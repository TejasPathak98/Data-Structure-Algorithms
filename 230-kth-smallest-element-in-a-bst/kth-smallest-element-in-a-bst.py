# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.val = -1
        def Inorder(root):
            if not root:
                return
            
            Inorder(root.left)
            self.cnt += 1
            if self.cnt == k:
                self.val = root.val
            Inorder(root.right)
        
        Inorder(root)
        return self.val


        