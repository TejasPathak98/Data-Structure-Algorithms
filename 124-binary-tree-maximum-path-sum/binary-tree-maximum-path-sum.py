# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        def helper(node):
            if not node:
                return 0
            
            maxleftpath = max(helper(node.left),0)
            maxrightpath = max(helper(node.right),0)

            maxifnodeisRoot = node.val + maxleftpath + maxrightpath
            self.final_sum = max(self.final_sum,maxifnodeisRoot)
            return node.val + max(maxleftpath,maxrightpath)

        self.final_sum = float("-inf")
        helper(root)
        return self.final_sum

