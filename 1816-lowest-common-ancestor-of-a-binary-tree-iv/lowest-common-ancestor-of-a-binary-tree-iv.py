# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root is None:
            return root
        
        # if len(nodes) == 1:
        #     return nodes[0]
        
        if root in nodes:
            return root
        
        l = self.lowestCommonAncestor(root.left, nodes)
        r = self.lowestCommonAncestor(root.right, nodes)

        if l and r:
            return root
        
        return l if l else r