# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodes = []

        def InOrder(node):
            if not node:
                return
            
            InOrder(node.left)
            nodes.append(node.val)
            InOrder(node.right)

        InOrder(root)
        
        return nodes[k - 1]