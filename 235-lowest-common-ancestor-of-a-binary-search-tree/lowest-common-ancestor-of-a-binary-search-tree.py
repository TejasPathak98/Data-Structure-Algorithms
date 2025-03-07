# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root is None:
        #     return None
        # if root == p or root == q:
        #     return root
        # if p is None:
        #     return q
        # if q is None:
        #     return p
        
        # l = self.lowestCommonAncestor(root.left, p, q)
        # r = self.lowestCommonAncestor(root.right, p, q)

        # if l and r:
        #     return root
        
        # return l if l else r

        # #O(N) ; O(N)

        parent = {} #for buidling the parent map
        stack = [root] #for iterative dfs

        while stack:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set() #parent set of p right up till the root
        while p:
            ancestors.add(p)
            p = parent.get(p)

        while q not in ancestors: #Going up p's ancestors for checking the lca
            q = parent.get(q)

        return q
