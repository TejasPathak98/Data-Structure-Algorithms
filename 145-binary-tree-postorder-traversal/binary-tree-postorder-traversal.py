# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []

        sol = []
        bag = [root]

        while bag:
            root = bag.pop()
            sol.append(root.val)

            if root.left:
                bag.append(root.left)
            
            if root.right:
                bag.append(root.right)
        
        return sol[::-1]
        