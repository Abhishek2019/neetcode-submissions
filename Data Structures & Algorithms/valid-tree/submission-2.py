from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True
        
        grid = {}

        if len(edges) != n-1:
            return False

        for i,j in edges:
            
            if i not in grid:
                grid[i] = []

            if j not in grid:
                grid[j] = []

            grid[i].append(j)
            grid[j].append(i)

        visited = [0]*n

        q = deque([0])
        visited[0] = 1

        while q:

            node = q.popleft()

            for ch in grid[node]:

                if visited[ch] == 0:

                    q.append(ch)
                    visited[ch] = 1

        
        for i in visited:
            if i != 1:
                return False

        return True






        


        


        