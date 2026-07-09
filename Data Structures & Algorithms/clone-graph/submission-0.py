"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        visited = {}

        q = deque([node])
        visited[node] = Node(node.val, neighbors=[])

        while q:

            curr_node = q.pop()

            for child_node in curr_node.neighbors:
                
                if child_node not in visited:
                    visited[child_node] = Node(child_node.val, [])

                    visited[curr_node].neighbors.append(visited[child_node])

                    q.append(child_node)
                else:
                    visited[curr_node].neighbors.append(visited[child_node])

        return visited[node]


            


            
