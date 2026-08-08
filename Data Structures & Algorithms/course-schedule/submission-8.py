from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        check = [0 for i in range(numCourses)]
        for a,b in prerequisites:
            
            graph[b].append(a)
            check[a]+=1

        visited = set([i for i in range(numCourses) if check[i] == 0])

        print(visited)
        q = deque(visited)

        while q:

            course = q.pop()
            if check[course] !=0:
                continue
            for ch in graph[course]:

                check[ch]-=1
                if check[ch] == 0:
                    visited.add(ch)
                    q.append(ch)
                    

        if len(visited) != numCourses:
            return False
        return True


        


        



