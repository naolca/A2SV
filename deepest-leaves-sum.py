# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def recursion(root):
            if not root:return 0
            return max(1+recursion(root.left),1+recursion(root.right))
        deepest=recursion(root)


        res=0
        def dfs(node,depth):
            nonlocal res,deepest
            if not node.left and not node.right:
                if depth==deepest:
                    res+=node.val
                return
            if node.right:
                dfs(node.right,depth+1)
            if node.left:
                dfs(node.left,depth+1)
        dfs(root,1)
        return res