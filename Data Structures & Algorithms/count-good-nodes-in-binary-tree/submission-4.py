# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_till_now):

            if not node:
                return 0

            count = 0

            if node.val >=max_till_now:
                count=1
                max_till_now = node.val
            
            lc = dfs(node.left, max_till_now)
            rc = dfs(node.right, max_till_now)

            return count+lc+rc






        out = dfs(root, root.val)

        return out


        