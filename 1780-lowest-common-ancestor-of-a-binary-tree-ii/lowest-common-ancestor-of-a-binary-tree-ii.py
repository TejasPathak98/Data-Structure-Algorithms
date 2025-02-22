# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node,p,q):
            if not node:
                return None,False,False
            
            left_lca,left_p,left_q = dfs(node.left,p,q)
            right_lca,right_p,right_q = dfs(node.right,p,q)

            mid_p = (node == p)
            mid_q = (node == q)
            found_p = left_p or right_p or mid_p
            found_q = left_q or right_q or mid_q

            if node == p or node == q:
                return node,found_p,found_q
            
            if left_lca and right_lca:
                return node,found_p,found_q
            
            if left_lca:
                return left_lca,found_p,found_q
            
            if right_lca:
                return right_lca,found_p,found_q
            
            return None,found_p,found_q
        
        the_node,found_p,found_q = dfs(root,p,q)
        
        return the_node if found_p and found_q else None

        #O(N) ; O(1)
        

        