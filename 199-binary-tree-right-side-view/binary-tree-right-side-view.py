# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        def helper(root,depth):
            if root.left:
                helper(root.left,depth + 1)
            d[depth] = root.val
            if root.right:
                helper(root.right,depth + 1)
        if root:
            helper(root,0)
        return [d[i] for i in sorted(d.keys())]
        