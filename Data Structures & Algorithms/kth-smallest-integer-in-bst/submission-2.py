# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.val = 0
        def dfs(node, rank):
            if not node:
                return rank

            left = dfs(node.left, rank)
            rank=left+1
            if rank == k:

                self.val = node.val
            right = dfs(node.right, rank)
        
            return right

        dfs(root,0)
        return self.val