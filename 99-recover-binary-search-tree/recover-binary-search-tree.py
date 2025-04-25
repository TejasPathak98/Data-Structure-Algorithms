# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nodes = []

        def InOrder(node):
            if not node:
                return
            InOrder(node.left)
            nodes.append(node)
            InOrder(node.right)
        
        InOrder(root)
        first = second = None

        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if first == None:
                    first  = nodes[i]

                second = nodes[i + 1]


        first.val , second.val = second.val , first.val 