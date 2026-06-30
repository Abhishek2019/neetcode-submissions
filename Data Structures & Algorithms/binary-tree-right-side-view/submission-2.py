# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        q = deque([root])

        out = []
        while q:

            lev = len(q)

            for i in range(lev):
                
                curr_node = q.popleft()
                if i == 0:
                    out.append(curr_node.val)

                if curr_node.right:
                    q.append(curr_node.right)
                
                if curr_node.left:
                    q.append(curr_node.left)

                



        return out


        
