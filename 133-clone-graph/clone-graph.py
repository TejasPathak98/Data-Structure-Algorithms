"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.my_dict = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node in self.my_dict:
            return self.my_dict[node]
        
        if not node:
            return None
        
        new_node = Node(node.val)
        self.my_dict[node] = new_node

        for neighbor in node.neighbors:
            if neighbor in self.my_dict:
                new_node.neighbors.append(self.my_dict[neighbor])
            else:
                new_node.neighbors.append(self.cloneGraph(neighbor))
        
        return new_node
                
        


        