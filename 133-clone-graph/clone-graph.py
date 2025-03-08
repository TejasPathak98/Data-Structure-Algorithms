"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # def __init__(self):
    #     self.graph_dict = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None
        
    #     if node in self.graph_dict:
    #         return self.graph_dict[node]
        
    #     new_node = Node(node.val)

    #     self.graph_dict[node] = new_node

    #     for neighbor in node.neighbors:
    #         new_node.neighbors.append(self.cloneGraph(neighbor))
        
    #     return new_node

    # #O(V + E) ; O(V)

        if not node:
            return None
        
        old_to_new = {node : Node(node.val)}
        queue = deque([node])

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                old_to_new[curr_node].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]


