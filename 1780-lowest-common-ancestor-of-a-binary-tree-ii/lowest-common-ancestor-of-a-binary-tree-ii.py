# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca_node(node):

            if not node:
                return None,False,False
            
            left_node , left_has_p , left_has_q = lca_node(node.left)

            if left_node:
                return left_node,True,True
            

            right_node , right_has_p , right_has_q = lca_node(node.right)

            if right_node:
                return right_node,True,True

            
            node_has_p = (node == p) or left_has_p or right_has_p
            node_has_q = (node == q) or left_has_q or right_has_q

            if node_has_p and node_has_q:

                return node,node_has_p,node_has_q
            
            return None,node_has_p,node_has_q


        lca , has_p , has_q = lca_node(root)
        return lca if has_p and has_q else None
                