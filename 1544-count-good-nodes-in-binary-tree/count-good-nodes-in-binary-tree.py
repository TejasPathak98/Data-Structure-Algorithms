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
    #     self.dfs(root,[])
    #     return self.max_count

    # def dfs(self,root,nodes):
    #     if root is None:
    #         return

    #     if len(nodes) == 0:
    #         self.max_count += 1
    #     else:
    #         if root.val >= max(nodes):
    #             self.max_count += 1
        
    #     nodes.append(root.val)
        
    #     self.dfs(root.left,nodes)
    #     self.dfs(root.right, nodes)

    #     nodes.pop()

    # #O(N); O(N)

        queue = deque([(root,float("-inf"))])
        max_count = 0

        while queue:
            node,max_so_far = queue.popleft()
            if node.val >= max_so_far:
                max_count += 1
            
            if node.left:
                queue.append((node.left,max(max_so_far,node.val)))
            if node.right:
                queue.append((node.right,max(max_so_far,node.val)))

        return max_count
            

        
