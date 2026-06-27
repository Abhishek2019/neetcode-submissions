class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        grid = {}

        for i,j in edges:
            
            if i not in grid:
                grid[i] = []

            if j not in grid:
                grid[j] = []

            grid[i].append(j)
            grid[j].append(i)

        out = 0
        visited = [0]*n

        def dfs(node):
            nonlocal visited

            if node in grid:

                for ch in grid[node]:
                    if visited[ch] == 0:
                        
                        visited[ch] = 1
                        dfs(ch)

            
        for i in range(n):

            if visited[i] != 1:
                visited[i] = 1
                dfs(i)
                out+=1

        return out




        

        