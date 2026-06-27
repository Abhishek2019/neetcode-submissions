# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.status = False

        def isSubTree(r, sub):

            if not r and not sub:
                return True
            
            if not r or not sub:
                return False

            
            if r.val != sub.val:
                return False

            
            return isSubTree(r.left, sub.left) and isSubTree(r.right, sub.right)


        def dfs(root, subRoot):

            if not root:
                return None

            if root.val == subRoot.val:

                out = isSubTree(root, subRoot)

                if out == True:
                    self.status = True
                    return None


            dfs(root.left, subRoot)
            dfs(root.right, subRoot)

            return root, subRoot
        
        dfs(root, subRoot)
        return self.status

