# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        level_sum = defaultdict(int)

        def dfs1(node,level):
            if not node:
                return
            
            level_sum[level] += node.val
            dfs1(node.left,level + 1)
            dfs1(node.right,level + 1)
        
        dfs1(root,0)

        def dfs2(node,level):
            if node:
                node.val = level_sum[level] - node.val

                if node.left and node.right:
                    sibling_sum = node.left.val + node.right.val
                    node.left.val = node.right.val = sibling_sum
                
                dfs2(node.left,level + 1)
                dfs2(node.right,level + 1)

        
        dfs2(root,0)

        return root