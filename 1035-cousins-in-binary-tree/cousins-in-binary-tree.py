# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth = defaultdict(set)
        parent_map = {}
        depth_flag = False

        def dfs_depth(node,level):
            depth[level].add(node.val)

            if node.left:
                parent_map[node.left.val] = node.val
                dfs_depth(node.left,level + 1)
            if node.right:
                parent_map[node.right.val] = node.val
                dfs_depth(node.right,level + 1)

        dfs_depth(root, 0)

        for level,nodes in depth.items():
            if x in nodes and y in nodes:
                depth_flag = True
                break
        
        if not depth_flag or (parent_map[x] == parent_map[y]):
            return False

        return True

        
        

        

        


        

