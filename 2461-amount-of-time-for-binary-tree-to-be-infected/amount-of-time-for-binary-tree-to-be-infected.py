# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        
        graph = defaultdict(list)

        def build_graph(node,parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)

        build_graph(root, None)
        queue = deque([start])
        time = -1
        visited =set([start])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
            time += 1
        

        return time
