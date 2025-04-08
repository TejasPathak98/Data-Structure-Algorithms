# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root.left is None and root.right is None:
            return [root.val]
        
        #left boundary

        self.lb = []

        def dfs_left_boundary(node):
            if not node:
                return
            
            self.lb.append(node.val)

            if node.left:
                dfs_left_boundary(node.left)
            else:
                if node.right:
                    dfs_left_boundary(node.right)

        dfs_left_boundary(root.left)
        self.lb = self.lb[:-1]

        print(self.lb)

        self.rb = []

        def dfs_right_boundary(node):
            if not node:
                return
            
            self.rb.append(node.val)

            if node.right:
                dfs_right_boundary(node.right)
            else:
                if node.left:
                    dfs_right_boundary(node.left)

        dfs_right_boundary(root.right)
        self.rb = self.rb[:-1]
        self.rb = self.rb[::-1]

        print(self.rb)

        self.leaves = []

        def dfs_leaves(node):
            if not node:
                return
            
            if node.left is None and node.right is None:
                self.leaves.append(node.val)
            
            if node.left:
                dfs_leaves(node.left)
            
            if node.right:
                dfs_leaves(node.right)

        dfs_leaves(root)
        print(self.leaves)

        
        self.result = [root.val]
        self.result.extend(self.lb)
        self.result.extend(self.leaves)
        self.result.extend(self.rb)

        return self.result



