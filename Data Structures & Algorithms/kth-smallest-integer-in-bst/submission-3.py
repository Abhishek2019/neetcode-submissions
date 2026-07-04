# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node,count):

            if not node:
                return None,count


            lval,lcount = dfs(node.left, count)

            if lcount == k:
                return lval, lcount

            count = lcount+1

            if count == k:
                return node.val, count

            rval,rcount = dfs(node.right, count)

            if rcount == k:
                return rval, rcount

            return node.val, rcount


        out,_ = dfs(root,0)
        return out
        