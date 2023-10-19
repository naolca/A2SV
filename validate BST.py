# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res=self.recursion(root)
        d=Counter(res)

        return True if (len(d)==len(res) and res==sorted(res)) else False
        

    def recursion(self,root):
        if not root:
            return []
        left=self.recursion(root.left)
        right=self.recursion(root.right)
        return left+[root.val]+right
    
    
