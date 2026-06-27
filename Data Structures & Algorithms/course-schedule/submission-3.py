from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        grid = [[0] * n for _ in range(n)]

        # course -> prerequisite
        for course, pre in prerequisites:
            grid[course][pre] = 1

        prereq_cnt = [sum(grid[i]) for i in range(n)]          # row sums
        q = deque([i for i in range(n) if prereq_cnt[i] == 0]) # no prereqs

        taken = 0
        while q:
            i = q.popleft()
            taken += 1

            # remove i as a prerequisite from any course c that has edge c -> i
            for c in range(n):
                if grid[c][i] == 1:
                    grid[c][i] = 0
                    prereq_cnt[c] -= 1
                    if prereq_cnt[c] == 0:
                        q.append(c)

        return taken == n
