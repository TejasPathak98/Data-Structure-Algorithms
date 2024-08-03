# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(0,0,root)])
        node_list = []

        while queue:
            x,y,node = queue.popleft()
            if node:
                node_list.append((x,y,node.val))
                queue.append((x - 1,y + 1,node.left))
                queue.append((x + 1,y + 1,node.right))
            
        node_list = sorted(node_list)

        dic = defaultdict(list) 

        for x,y,val in node_list:
            dic[x].append(val) 
        
        return [dic[x] for x in sorted(dic)]





        