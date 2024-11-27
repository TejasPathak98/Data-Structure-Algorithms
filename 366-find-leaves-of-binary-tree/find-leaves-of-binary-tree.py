# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def recurse(root):
            if not root:
                return None
            if not(root.left or root.right):
                res[-1].append(root.val)
                return None
            root.left = recurse(root.left)
            root.right = recurse(root.right)
            return root
        while root:
            res.append([])
            root = recurse(root)
        return res
        