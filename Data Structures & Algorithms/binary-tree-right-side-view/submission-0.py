# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.out = []

        def dfs(node, dep):

            if not node:
                return None


            if dep == len(self.out):
                self.out.append(node.val)
            
            dfs(node.right, dep+1)
            dfs(node.left, dep+1)

        dfs(root,0)
        return self.out