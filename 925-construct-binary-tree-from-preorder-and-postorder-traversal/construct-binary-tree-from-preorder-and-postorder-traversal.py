# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #the main idea here is that we get the root of the left subtree (2nd element of preorder) and hence the size of the left sub tree in postorder
        if not preorder:
            return None

        n = len(preorder)
        if n == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        left_size = postorder.index(preorder[1]) + 1

        root.left = self.constructFromPrePost(preorder[1:left_size + 1], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size + 1:], postorder[left_size:-1])

        return root