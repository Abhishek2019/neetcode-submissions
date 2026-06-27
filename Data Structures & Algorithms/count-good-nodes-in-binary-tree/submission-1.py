# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def dfs(node, m):

            if not node:
                return None

            if node.val >= m:

                self.count+=1
            
                m = node.val

            dfs(node.left,m)
            dfs(node.right,m)

            return None


        dfs(root, float('-inf'))
        return self.count



        