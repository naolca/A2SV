# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res=0
        def dfs(node,parents):
            nonlocal res
            if not node:
                return
            # print(node.val,parents)
            if len(parents)>=2 and parents[-2]%2==0:
                res+=node.val
            china=parents.copy()
            china.append(node.val)
            if node.left:
                dfs(node.left,china)
            if node.right:
                dfs(node.right,china)
        dfs(root,[])
        return res