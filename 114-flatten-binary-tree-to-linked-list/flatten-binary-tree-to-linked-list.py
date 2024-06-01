# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root 
        if root.left is None and root.right is None:
            return root 
        
        li = [] 

        def helper(root):
            if root is None:
                return

            li.append(root)
            helper(root.left) 
            helper(root.right) 

        helper(root)
        

        new_root = li[0]
        r = new_root
        new_root.left = None

        for i in range(1,len(li)):
            new_root.right = li[i]
            new_root = new_root.right
            new_root.left = None
        
        return r



        
        