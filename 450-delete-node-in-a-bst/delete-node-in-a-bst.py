# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                x = root.right
                while x.left:
                    x = x.left
                root.val = x.val
                root.right = self.deleteNode(root.right, root.val)
                return root
        