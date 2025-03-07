# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_count = 0 

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root,[])
        return self.max_count

    def dfs(self,root,nodes):
        print("Break")
        if root is None:
            return

        if len(nodes) == 0:
            print(root.val)
            self.max_count += 1
        else:
            if root.val >= max(nodes):
                print(root.val)
                self.max_count += 1
        
        nodes.append(root.val)
        
        self.dfs(root.left,nodes)
        self.dfs(root.right, nodes)

        nodes.pop()

        
