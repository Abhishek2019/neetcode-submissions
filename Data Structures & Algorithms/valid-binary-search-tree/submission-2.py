# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node):
            if not node:

                return float('inf'), float('-inf'), True

            
            ll,lr,sl = dfs(node.left)
            rl,rr,sr = dfs(node.right)

            s = sl and sr and (lr<node.val<rl)

            return min(node.val, ll,rl), max(node.val,rr,lr), s


        out,x,y = dfs(root)
        return y
        