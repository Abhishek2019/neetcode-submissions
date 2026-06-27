# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque([root])

        out = []
        while q:

            lev = len(q)

            lev_arr = []

            for _ in range(lev):

                x = q.popleft()
                lev_arr.append(x.val)

                if x.left:
                    q.append(x.left)

                if x.right:
                    q.append(x.right)

            out.append(lev_arr)

        return out

            

