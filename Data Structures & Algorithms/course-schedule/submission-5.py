from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        
        grid = {}

        indeg = [0]*numCourses

        for i,j in prerequisites:

            if j not in grid:
                grid[j] = []
            
            grid[j].append(i) 
            indeg[i]+=1

        
        zero_degree = [i for i in range(numCourses) if indeg[i]==0 ]

        if len(zero_degree) == 0:
            return False

        q = deque(zero_degree)

        while q:

            parent = q.popleft()

            if parent not in grid:
                continue

            for child in grid[parent]:

                indeg[child]-=1

                if indeg[child] == 0:
                    q.append(child)


        if sum(indeg) == 0:
            return True
        
        return False



