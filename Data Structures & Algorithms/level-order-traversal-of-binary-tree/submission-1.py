# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        out = []

        if not root:
            return []

        q = deque([root])
        

        while q:

            lev = len(q)
            lev_list = []
            for _ in range(lev):

                curr_node = q.popleft()

                lev_list.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            out.append(lev_list)

        return out
            





        return out


        