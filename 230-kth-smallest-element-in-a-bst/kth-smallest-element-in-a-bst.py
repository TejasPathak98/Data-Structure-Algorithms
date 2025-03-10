# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    #     self.inorder(root)
    #     return self.arr[k - 1]
    
    # def inorder(self,root):
    #     if not root:
    #         return

    #     self.inorder(root.left)
    #     self.arr.append(root.val)
    #     self.inorder(root.right)

    # #O(N) ; O(N)

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            root = root.right

        return -1

