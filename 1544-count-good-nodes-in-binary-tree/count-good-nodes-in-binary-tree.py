# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.good_nodes = 0

        def dfs(node,prev):
            if not node:
                return
            
            if  len(prev) == 0  or node.val >= max(prev):
                print(node.val, prev)
                self.good_nodes += 1
            
            if node.left:
                dfs(node.left,prev + [node.val])
            if node.right:
                dfs(node.right,prev + [node.val])

        dfs(root,[])

        return self.good_nodes
