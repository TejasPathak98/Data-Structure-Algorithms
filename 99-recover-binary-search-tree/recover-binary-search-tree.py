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
        #1,3,2,4 ; 1,2,3,4
        #3,2,1 : 1,2,3

        nodes = []

        def Inorder(node):
            if node is None:
                return

            Inorder(node.left)

            nodes.append(node)

            Inorder(node.right)
        
        Inorder(root)
        print(nodes)

        first = second = None

        for i in range(len(nodes) - 1):
            if nodes[i].val < nodes[i + 1].val:
                continue
            else:
                if first == None:
                    first = nodes[i]
                
                second = nodes[i + 1]
        
        first.val , second.val = second.val , first.val


