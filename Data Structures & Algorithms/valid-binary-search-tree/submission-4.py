# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import numpy as np

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return True, -np.inf, np.inf

            

            lstatus, ll,lr = dfs(node.left)
            rstatus, rl,rr = dfs(node.right)

            max_left = ll
            min_right = rr

            print(max_left, node.val, min_right, lstatus, rstatus)

            if lstatus and rstatus and max_left<node.val<min_right:

                return True, max(ll,rl,node.val), min(node.val, rr,lr)
            else:
                return False,  max(ll,rl,node.val), min(node.val, rr,lr)








        out,_,_ = dfs(root)
        return out


        